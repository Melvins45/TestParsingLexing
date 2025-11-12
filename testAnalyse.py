from analyseLexicale import MyLexer

lexer = MyLexer()
lexer.build()

samples_valids = [
    """
    program
var
 var:integer;
 
begin
 i := 12;
       if ui := fr then while t = r do f
end.""",
"""
var
 var:integer;
 
begin
 io := 789 + iuo
end.""",
"""
var
 var:integer;
 
var var i-78 var jui
"""
]


samples_invalids = [
    """
    program
var
 £var:integer;
 
begin
 i := 12;
       if ui := fr then while t = r do f
end.""",
"""
var
 var:integer;
 
begin
 io != 789 + iuo program
end.""",
"""
var
 $var:integer;
 
var var i-7bgyu8 programbegin 7var jui
"""
]

print("\nExemples valides : \n")
for sample in samples_valids :
    lexer.test(sample)
    print()

print("\nExemples invalides : \n")
for sample in samples_invalids :
    lexer.test(sample)
    print()