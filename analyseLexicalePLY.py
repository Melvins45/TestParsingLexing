import ply.lex as lex

class Lexer:
    # Liste des mots réservés
    reserved = {
        'program': 'PROGRAM',
        'var': 'VAR',
        'integer': 'INTEGER',
        'boolean': 'BOOLEAN',
        'begin': 'BEGIN',
        'end': 'END',
        'if': 'IF',
        'then': 'THEN',
        'else': 'ELSE',
        'while': 'WHILE',
        'do': 'DO',
        'true': 'TRUE',
        'false': 'FALSE',
        'and': 'AND',
        'or': 'OR'
    }

    # Liste des tokens reconnus
    tokens = [
        'ID', 'NUMBER',
        'PLUS', 'MINUS', 'TIMES', 'DIV',
        'EQUAL', 'NEQ', 'LT', 'LE', 'GT', 'GE',
        'ASSIGN',
        'SEMI', 'COLON', 'COMMA', 'DOT', 'LPAREN', 'RPAREN'
    ] + list(reserved.values())

    # Expressions régulières liées à chaque token
    t_PLUS    = r'\+'
    t_MINUS   = r'-'
    t_TIMES   = r'\*'
    t_DIV     = r'/'
    t_EQUAL   = r'='
    t_NEQ     = r'<>'
    t_LT      = r'<'
    t_LE      = r'<='
    t_GT      = r'>'
    t_GE      = r'>='
    t_ASSIGN  = r':='
    t_SEMI    = r';'
    t_COLON   = r':'
    t_COMMA   = r','
    t_DOT     = r'\.'
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'

    t_ignore = ' \t\r'

    # Pour certains tokens particuliers, utiliser des fonctions pour manipuler les valeurs lues
    def t_ID(self, t):
        r'[a-zA-Z][a-zA-Z0-9_]*'
        t.type = self.reserved.get(t.value, 'ID') # Pour distinguer les mots-clés du langage des identificateurs ordinaires.
        return t

    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value) # Pour convertir l'entrée lue en entier 
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value) # Pour sauvegarder le numéro actuel de la ligne

    # Pour gérer les erreurs
    def t_error(self, t):
        raise SyntaxError(f"Caractère illégal à la ligne {t.lineno} : '{t.value[0]}'")


    # Construire l'analyseur lexical à partir des règles de la classe 
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Reconnaitre tous les tokens dans l'entrée donnée et les ressortir
    def tokenize(self, data):
        self.lexer.input(data)
        return list(self.lexer)
