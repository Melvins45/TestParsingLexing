import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analyseSyntaxiquePLY import Parser

def test_simple_program():
    code = """
    program test;
    var x : integer;
    begin
        x := 5;
    end.
    """
    parser = Parser()
    result = parser.parse(code)
    assert result[0] == 'program'
    assert result[1] == 'test'
    assert isinstance(result[2], tuple)
