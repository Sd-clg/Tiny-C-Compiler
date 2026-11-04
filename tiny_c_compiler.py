import re

# ===== LEXER (Tokenizer) =====
def tokenize(code):
    tokens = []
    patterns = [
        ('NUMBER', r'\d+'),
        ('ID', r'[a-z]+'),
        ('OP', r'[+\-*/=]'),
        ('LPAREN', r'\('),
        ('RPAREN', r'\)'),
        ('LBRACE', r'\{'),
        ('RBRACE', r'\}'),
        ('SEMICOLON', r';'),
        ('SPACE', r'\s+'),
    ]
    
    regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in patterns)
    
    for match in re.finditer(regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind != 'SPACE':
            tokens.append((kind, value))
    
    return tokens

# ===== PARSER (Build Abstract Syntax Tree) =====
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    
    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None
    
    def consume(self):
        token = self.peek()
        self.pos += 1
        return token
    
    def parse_program(self):
        statements = []
        while self.peek():
            statements.append(self.parse_statement())
        return statements
    
    def parse_statement(self):
        # Simple: either assignment or declaration
        token = self.peek()
        
        if token[0] == 'ID':
            name = self.consume()[1]
            
            # Check if it's a declaration (int x) or assignment (x = 5)
            if self.peek()[0] == 'SEMICOLON':
                # Just "x;"
                self.consume()
                return ('DECL', name)
            else:
                # Must be assignment: x = ...
                self.consume()  # consume '='
                expr = self.parse_expr()
                self.consume()  # consume ';'
                return ('ASSIGN', name, expr)
    
    def parse_expr(self):
        left = self.parse_term()
        
        while self.peek() and self.peek()[0] == 'OP' and self.peek()[1] in ['+', '-']:
            op = self.consume()[1]
            right = self.parse_term()
            left = ('BINOP', op, left, right)
        
        return left
    
    def parse_term(self):
        left = self.parse_factor()
        
        while self.peek() and self.peek()[0] == 'OP' and self.peek()[1] in ['*', '/']:
            op = self.consume()[1]
            right = self.parse_factor()
            left = ('BINOP', op, left, right)
        
        return left
    
    def parse_factor(self):
        token = self.peek()
        
        if token[0] == 'NUMBER':
            return ('NUM', int(self.consume()[1]))
        elif token[0] == 'ID':
            return ('VAR', self.consume()[1])
        elif token[0] == 'LPAREN':
            self.consume()  # (
            expr = self.parse_expr()
            self.consume()  # )
            return expr

# ===== CODE GENERATOR =====
class CodeGen:
    def __init__(self, ast):
        self.ast = ast
        self.code = []
        self.vars = {}
        self.temp_count = 0
    
    def new_temp(self):
        self.temp_count += 1
        return f"temp{self.temp_count}"
    
    def generate(self):
        self.code.append("# Generated Code\n")
        
        for stmt in self.ast:
            self.gen_stmt(stmt)
        
        return '\n'.join(self.code)
    
    def gen_stmt(self, stmt):
        if stmt[0] == 'DECL':
            var = stmt[1]
            self.vars[var] = None
            self.code.append(f"{var} = 0")
        
        elif stmt[0] == 'ASSIGN':
            var = stmt[1]
            expr = stmt[2]
            result = self.gen_expr(expr)
            self.code.append(f"{var} = {result}")
    
    def gen_expr(self, expr):
        if expr[0] == 'NUM':
            return str(expr[1])
        
        elif expr[0] == 'VAR':
            return expr[1]
        
        elif expr[0] == 'BINOP':
            op = expr[1]
            left = self.gen_expr(expr[2])
            right = self.gen_expr(expr[3])
            temp = self.new_temp()
            self.code.append(f"{temp} = {left} {op} {right}")
            return temp

# ===== MAIN =====
if __name__ == "__main__":
    # Example input
    code = """
    x = 5;
    y = 3;
    z = x + y * 2;
    """
    
    print("=== INPUT ===")
    print(code)
    
    print("\n=== TOKENS ===")
    tokens = tokenize(code)
    for token in tokens:
        print(token)
    
    print("\n=== AST ===")
    parser = Parser(tokens)
    ast = parser.parse_program()
    for node in ast:
        print(node)
    
    print("\n=== GENERATED CODE ===")
    codegen = CodeGen(ast)
    output = codegen.generate()
    print(output)
