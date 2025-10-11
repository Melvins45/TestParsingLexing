import ply.lex as lex

class MyLexer(object):
    # List of reserved words
    reserved = { 
        "and" : "AND", 
        "array" : "ARRAY", 
        "begin" : "BEGIN", 
        "boolean" : "BOOLEAN", 
        "case" : "CASE", 
        "char" : "CHAR", 
        "const" : "CONST", 
        "div" : "DIV", 
        "do" : "DO", 
        "downto" : "DOWNTO",
        "else" : "ELSE", 
        "end" : "END", 
        "file" : "FILE", 
        "for" : "FOR", 
        "function" : "FUNCTION", 
        "goto" : "GOTO", 
        "if" : "IF", 
        "in" : "IN", 
        "integer" : "INTEGER",
        "label" : "LABEL", 
        "mod" : "MOD", 
        "nil" : "NIL", 
        "not" : "NOT", 
        "of" : "OF", 
        "or" : "OR", 
        "packed" : "PACKED", 
        "procedure" : "PROCEDURE", 
        "program" : "PROGRAM",
        "real" : "REAL", 
        "record" : "RECORD", 
        "repeat" : "REPEAT", 
        "set" : "SET", 
        "string" : "STRING",
        "then" : "THEN", 
        "to" : "TO", 
        "type" : "TYPE", 
        "until" : "UNTIL", 
        "var" : "VAR", 
        "while" : "WHILE",
        "with" : "WITH"
    }
    
    # List of token names.   This is always required
    tokens = [
       'NUMBER',
       'PLUS',
       'MINUS',
       'TIMES',
       'DIVIDE',
       'LPAREN',
       'RPAREN',
       'IDENTIFIER' # Pour les noms de variables
    ]  + list(reserved.values())

    # Regular expression rules for simple tokens
    t_PLUS             = r'\+'
    t_MINUS            = r'-'
    t_TIMES            = r'\*'
    t_DIVIDE           = r'/'
    t_LPAREN           = r'\('
    t_RPAREN           = r'\)'
    
    # t_ADD              = r'add'
    # t_ARRAY            = r'array'
    # t_BEGIN            = r'begin'
    # t_BOOLEAN          = r'boolean'
    # t_CASE             = r'case'
    # t_CHAR             = r'char'
    # t_CONST            = r'const'
    # t_DIV              = r'div'
    # t_DO               = r'do'
    # t_DOWNTO           = r'downto'
    # t_ELSE             = r'else'
    # t_END              = r'end'
    # t_FILE             = r'file'
    # t_FOR              = r'for'
    # t_FUNCTION         = r'function'
    # t_FOR              = r'goto'
    # t_IF               = r'if'
    # t_IN               = r'in'
    # t_INTEGER          = r'integer'
    # t_LABEL            = r'label'
    # t_MOD              = r'mod'
    # t_NIL              = r'nil'
    # t_NOT              = r'not'
    # t_OF               = r'of'
    # t_OR               = r'or'
    # t_PACKED           = r'packed'
    # t_PROCEDURE        = r'procedure'
    # t_PROGRAM          = r'program'
    # t_REAL             = r'real'
    # t_RECORD           = r'record'
    # t_REPEAT           = r'repeat'
    # t_SET              = r'set'
    # t_STRING           = r'string'
    # t_THEN             = r'then'
    # t_TO               = r'to'
    # t_TYPE             = r'type'
    # t_UNTIL            = r'until'
    # t_VAR              = r'var'
    # t_WHILE            = r'while'
    # t_WITH             = r'with'

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
m = MyLexer()
m.build()           # Build the lexer
# m.test("3 a if + 4")     # Test it
m.test("""Program CaseOfNoElseSamples;
 
Const
 A = 7;
 
Var
 CaseNotDefault:Boolean;
 
BEGIN
 CaseNotDefault := False;
 Case A Of
  0,1,2: Begin
   CaseNotDefault := True;
   WriteLn('0, 1, 2');
  End;
  3:Begin
   CaseNotDefault := True;
   WriteLn('3');
  End;
  4:Begin
   CaseNotDefault := True;
   WriteLn('4');
  End;
 End;
 If Not CaseNotDefault Then Begin
  WriteLn('Autre valeur');
 End;
END.""")     # Test it