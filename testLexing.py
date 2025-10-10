import ply.lex as lex

class MyLexer(object):
    # List of reserved words
    reserved = [ s.upper() for s in [
    "and", "array", "begin", "case", "char", "const", "div", "do", "downto",
    "else", "end", "file", "for", "function", "goto", "if", "in", "integer",
    "label", "mod", "nil", "not", "of", "or", "packed", "procedure", "program",
    "record", "repeat", "set", "then", "to", "type", "until", "var", "while",
    "with", "boolean", "real", "string"
    ]]
    
    # List of token names.   This is always required
    tokens = [
       'NUMBER',
       'PLUS',
       'MINUS',
       'TIMES',
       'DIVIDE',
       'LPAREN',
       'RPAREN',
    ]
    tokens.extend(reserved)

    # Regular expression rules for simple tokens
    t_PLUS    = r'\+'
    t_MINUS   = r'-'
    t_TIMES   = r'\*'
    t_DIVIDE  = r'/'
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'
    
    t_ADD     = r'add'
    t_ARRAY   = r'array'
    t_BEGIN   = r'begin'
    t_CASE    = r'case'
    t_CHAR    = r'char'
    t_CONST   = r'const'
    t_DIV     = r'div'
    t_DO      = r'do'
    t_DOWNTO  = r'do'
    t_IF      = r'if'

    # A regular expression rule with some action code
    # Note addition of self parameter since we're in a class
    def t_NUMBER(self,t):
        r'\d+'
        t.value = int(t.value)
        return t

    # Define a rule so we can track line numbers
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

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
m = MyLexer()
m.build()           # Build the lexer
m.test("3 a if + 4")     # Test it