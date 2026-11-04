# Tiny C Compiler

## Description

**Tiny C Compiler** is a lightweight compiler for a simplified C-like language. It demonstrates the three core phases of compilation: lexical analysis (tokenizing), syntax analysis (parsing into an AST), and code generation (converting AST to executable code). This project parses basic variable declarations and assignments with arithmetic expressions.

## How to Run Online

1. Visit an online Python compiler like [Replit](https://replit.com) or [OnlineGDB](https://www.onlinegdb.com)
2. Copy the entire code into the editor
3. Click **Run**
4. View the tokenized output, AST, and generated code in the console

# What It Does

## The compiler performs four key operations:

Tokenization (Lexer) – Breaks input code into tokens (numbers, identifiers, operators)
Parsing (Parser) – Builds an Abstract Syntax Tree (AST) from tokens
Code Generation (CodeGen) – Converts the AST into executable Python code
Output – Prints each stage for debugging and understanding
Example: x = 5; y = 3; z = x + y * 2; is tokenized, parsed into an AST, and generates executable Python code.

## Run with GCC (Local Machine)

Since this project is written in Python, not C, use Python instead:
```bash
python code\_cleaned.py
Or with Python 3:

bash


python3 code\_cleaned.py
