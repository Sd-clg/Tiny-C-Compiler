Description
Tiny C Compiler is a lightweight compiler for a simplified C-like language. It demonstrates the three core phases of compilation: lexical analysis (tokenizing), syntax analysis (parsing into an AST), and code generation (converting AST to executable code).

How to Run Online (GDB or Online Compiler)
Visit an online Python compiler like Replit or OnlineGDB.
Copy the entire code into the editor.
Click Run.
View the tokenized output, AST, and generated code in the console.
No installation required — just paste and execute!

Run with GCC (Local Machine)
Since this project is written in Python, not C, use Python instead:

bash

python code_cleaned.py
Or, if you have Python 3:

bash

python3 code_cleaned.py
The script will execute the example code and display all compilation stages.

What It Does
The compiler performs four key operations:

Tokenization (Lexer) – Breaks input code into tokens (numbers, identifiers, operators).
Parsing (Parser) – Builds an Abstract Syntax Tree (AST) from tokens.
Code Generation (CodeGen) – Converts the AST into executable Python code.
Output – Prints each stage for debugging and understanding.
Example: The input x = 5; y = 3; z = x + y * 2; is tokenized, parsed into an AST, and generates executable Python code.
