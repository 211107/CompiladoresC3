from lark import Lark, Transformer, UnexpectedInput

# Gramática del analizador sintáctico
grammar = '''
    start: program

    program: command+

    command: "var" CNAME "int"
           | function
           | "stmt" "{" statement+ "}"
           | "imprimir(" ESCAPED_STRING ")"
           | "leer(" CNAME ")"
           | conditional
           | cycle
           | "romper"
           | CNAME "=" ESCAPED_STRING

    function: "fun" "main()" "{" statement+ "}"

    conditional: "si" CNAME ">=" ESCAPED_STRING "{" statement+ "}"
               | "sino" "{" statement+ "}"

    cycle: "mientras" "verdadero" "{" statement+ "}"

    statement: "imprimir(" ESCAPED_STRING ")"
             | "leer(" CNAME ")"
             | "var" CNAME "int"
             | "fun" "main()" "{" statement+ "}"
             | "stmt" "{" statement+ "}"
             | "si" CNAME ">=" ESCAPED_STRING "{" statement+ "}"
             | "sino" "{" statement+ "}"
             | "mientras" "verdadero" "{" statement+ "}"
             | "romper"

    ESCAPED_STRING: "\\"" /[^\\"]*/ "\\""
    %import common.CNAME
    %import common.WS
    %ignore WS
'''


class CodeTransformer(Transformer):
    def program(self, *args):
        return True

def parse_code(code):
    try:
        parser = Lark(grammar, parser='lalr', transformer=CodeTransformer())
        parser.parse(code)
        return True  # El código es válido
    except UnexpectedInput as e:
        return False  # El código es inválido
