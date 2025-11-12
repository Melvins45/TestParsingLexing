import ply.yacc as yacc
from analyseLexicalePLY import Lexer

class Parser:
    def __init__(self):
        self.lexer = Lexer()
        self.lexer.build()
        self.tokens = self.lexer.tokens
        self.parser = yacc.yacc(module=self)

    def parse(self, data):
        return self.parser.parse(data, lexer=self.lexer.lexer)

    def p_program(self, p):
        'program : PROGRAM ID SEMI block DOT'
        p[0] = ('program', p[2], p[4])

    def p_block(self, p):
        'block : declarations BEGIN statement_list END'
        p[0] = ('block', p[1], p[3])

    def p_declarations(self, p):
        '''declarations : VAR var_decl_list
                        | empty'''
        p[0] = p[2] if len(p) > 2 else []

    def p_var_decl_list(self, p):
        '''var_decl_list : var_decl_list var_decl
                         | var_decl'''
        p[0] = p[1] + [p[2]] if len(p) == 3 else [p[1]]

    def p_var_decl(self, p):
        'var_decl : ID COLON type SEMI'
        p[0] = ('var_decl', p[1], p[3])

    def p_type(self, p):
        '''type : INTEGER | BOOLEAN'''
        p[0] = p[1]

    def p_statement_list(self, p):
        '''statement_list : statement_list SEMI statement
                          | statement'''
        p[0] = p[1] + [p[3]] if len(p) == 4 else [p[1]]

    def p_statement(self, p):
        '''statement : assignment | if_statement | while_statement | compound_statement'''
        p[0] = p[1]

    def p_assignment(self, p):
        'assignment : ID ASSIGN expression'
        p[0] = ('assign', p[1], p[3])

    def p_if_statement(self, p):
        '''if_statement : IF expression THEN statement
                        | IF expression THEN statement ELSE statement'''
        p[0] = ('if', p[2], p[4]) if len(p) == 5 else ('if_else', p[2], p[4], p[6])

    def p_while_statement(self, p):
        'while_statement : WHILE expression DO statement'
        p[0] = ('while', p[2], p[4])

    def p_compound_statement(self, p):
        'compound_statement : BEGIN statement_list END'
        p[0] = ('compound', p[2])

    def p_expression(self, p):
        '''expression : expression relop expression
                      | simple_expression'''
        p[0] = ('binop', p[2], p[1], p[3]) if len(p) == 4 else p[1]

    def p_simple_expression(self, p):
        '''simple_expression : simple_expression addop term
                             | term'''
        p[0] = ('binop', p[2], p[1], p[3]) if len(p) == 4 else p[1]

    def p_term(self, p):
        '''term : term mulop factor
                | factor'''
        p[0] = ('binop', p[2], p[1], p[3]) if len(p) == 4 else p[1]

    def p_factor(self, p):
        '''factor : ID | NUMBER | TRUE | FALSE | LPAREN expression RPAREN'''
        p[0] = ('const', p[1]) if len(p) == 2 else p[2]

    def p_relop(self, p):
        '''relop : EQUAL | NEQ | LT | LE | GT | GE'''
        p[0] = p[1]

    def p_addop(self, p):
        '''addop : PLUS | MINUS | OR'''
        p[0] = p[1]

    def p_mulop(self, p):
        '''mulop : TIMES | DIV | AND'''
        p[0] = p[1]

    def p_empty(self, p):
        'empty :'
        p[0] = []

    def p_error(self, p):
        print(f"Syntax error at {p.value if p else 'EOF'}")
