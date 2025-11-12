import ply.lex as lex

class MyLexer(object):

    reserved = {
        "program" : "PROGRAM", 
        "var" : "VAR", 
        "begin" : "BEGIN", 
        "end" : "END", 
        "if" : "IF", 
        "else" : "ELSE", 
        "then" : "THEN", 
        "while" : "WHILE", 
        "do" : "DO"
    }

    # List of token names.   This is always required
    tokens = [
       'PROGRAM',
       'VAR',
       'INTEGER',
       'BEGIN',
       'END',
       'IF',
       'THEN',
       'ELSE',
       'WHILE',
       'DO',
       'ID', # Pour les noms de variables
       'NUMBER',
       'OP_ARITH',
       'OP_REL',
       'SYM',
    ]

    # Regular expression rules for simple tokens
    t_PROGRAM = r'program'
    t_VAR = r'var'
    t_INTEGER = r'integer'
    t_BEGIN = r'begin'
    t_END = r'end'
    t_IF = r'if'
    t_THEN = r'then'
    t_ELSE = r'else'
    t_WHILE = r'while'
    t_DO = r'do'
    t_OP_ARITH = r'\+|-|\*|/'
    t_OP_REL = r'=|<|>|<=|>=|<>'
    t_SYM = r';|:|:=|\.'

    # A regular expression rule with some action code
    # Note addition of self parameter since we're in a class
    def t_NUMBER(self,t):
        r'\d+'
        t.value = int(t.value)
        return t

    # Define a rule so we can track line numbers
    # def t_newline(self,t):
    #     r'\n+'
    #     t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t\n'

    # Error handling rule
    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def t_ID(self,t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value,'ID')    # Check for reserved words
        return t

    # Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Test it output
    def test(self,data):
        self.lexer.input(data)
        while True:
             tok = self.lexer.token()
             if not tok:
                 break
             print(tok)

# Build the lexer and try it out
if __name__ == "__main__" :
    m = MyLexer()
    m.build()           
    m.test("""
    var
    $var:integer;
    
    begin
    i := 12;
        if u0i := fr then while t = r do f
    end.""")     

    print("Tokens reconnus", m.tokens)