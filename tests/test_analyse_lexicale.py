import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from analyseLexicalePLY import Lexer

def test_tokenization_valid_sample_1():
    code = """
    program test;
    var x: integer;
    begin
        x := 42;
    end.
    """

    lexer = Lexer()
    lexer.build()
    tokens = lexer.tokenize(code)

    expected_types = [
        'PROGRAM', 'ID', 'SEMI',
        'VAR', 'ID', 'COLON', 'INTEGER', 'SEMI',
        'BEGIN',
        'ID', 'ASSIGN', 'NUMBER', 'SEMI',
        'END', 'DOT'
    ]

    # Récupérer les types de tokens reconnus
    actual_types = [token.type for token in tokens]

    # Vérifier si on a les mêmes tokens
    assert actual_types == expected_types

def test_tokenization_valid_sample_2():
    code = """
    program begin test;
        x := 42;
    end.
    """

    lexer = Lexer()
    lexer.build()
    tokens = lexer.tokenize(code)

    expected_types = [
        'PROGRAM', 'BEGIN', 'ID', 'SEMI',
        'ID', 'ASSIGN', 'NUMBER', 'SEMI',
        'END', 'DOT'
    ]

    # Récupérer les types de tokens reconnus
    actual_types = [token.type for token in tokens]

    # Vérifier si on a les mêmes tokens
    assert actual_types == expected_types

def test_tokenization_valid_sample_3():
    code = """
    program test;
    fg / frt
    """

    lexer = Lexer()
    lexer.build()
    tokens = lexer.tokenize(code)

    expected_types = [
        'PROGRAM', 'ID', 'SEMI',
        'ID', 'DIV', 'ID'
    ]

    # Récupérer les types de tokens reconnus
    actual_types = [token.type for token in tokens]

    # Vérifier si on a les mêmes tokens
    assert actual_types == expected_types

def test_tokenization_invalid_sample_1():
    code = """
    program test;
    var £x: integer;
    begin
        x := 42;
    end.
    """

    lexer = Lexer()
    lexer.build()
    
    # Vérifier si on recoit effectivement une erreur SyntaxError
    with pytest.raises(SyntaxError):
        lexer.tokenize(code)

def test_tokenization_invalid_sample_2():
    code = """
    p*µrogram test;
    var x: integer;
    begin
        x := 42;
    end.
    """

    lexer = Lexer()
    lexer.build()
    
    # Vérifier si on recoit effectivement une erreur SyntaxError
    with pytest.raises(SyntaxError):
        lexer.tokenize(code)

def test_tokenization_invalid_sample_3():
    code = """
    $£
    """

    lexer = Lexer()
    lexer.build()
    
    # Vérifier si on recoit effectivement une erreur SyntaxError
    with pytest.raises(SyntaxError):
        lexer.tokenize(code)

