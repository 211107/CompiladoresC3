import ply.lex as lex
from ply.lex import LexError

# resultado del análisis
resultado_lexema = []

reservada = (
    'var',
    'int',
    'fun',
    'mientras',
    'si',
    'sino',
    'romper',
    'imprimir',
    'leer',
)

tokens = reservada + (
    'ASIGNAR',
    'ENTERO',
    'MENORQUE',
    'MENORIGUAL',
    'MAYORQUE',
    'MAYORIGUAL',
    'IGUAL',
    'PARIZQ',
    'PARDER',
    'LLAIZQ',
    'LLADER',
    'LETRA',
    'NUMERO',
    'COMILLAS',
)

# Reglas de expresiones regulares para asignacion de  tokens
t_ASIGNAR = r'='
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_LLAIZQ = r'\{'
t_LLADER = r'\}'

def t_var(t):
    r'var'
    return t

def t_fun(t):
    r'fun'
    return t

def t_mientras(t):
    r'mientras'
    return t

def t_si(t):
    r'si'
    return t

def t_sino(t):
    r'sino'
    return t

def t_romper(t):
    r'romper'
    return t

def t_imprimir(t):
    r'imprimir'
    return t

def t_leer(t):
    r'leer'
    return t

def t_ENTERO(t):
    r'int'
    return t

def t_MENORIGUAL(t):
    r'<='
    return t

def t_MAYORIGUAL(t):
    r'>='
    return t

def t_IGUAL(t):
    r'=='
    return t

def t_LETRA(t):
    r'[a-zA-Z][a-zA-Z]*'
    if t.value in reservada:
        t.type = t.value  # Reconoce palabras clave
    return t

def t_NUMERO(t):
    r'\d+'  # Expresión regular para reconocer uno o más dígitos
    t.value = int(t.value)  # Convierte el valor a un entero
    return t

def t_COMILLAS(t):
    r'\"'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    #print("Comentario de múltiple línea")

def t_comments_ONELine(t):
    r'\/\/(.)*\n'
    t.lexer.lineno += 1
   # print("Comentario de una línea")

def t_ANY_error(t):
    estado = "Carácter no reconocido en la Línea {:4} Valor {:16} Posición {:4}".format(str(t.lineno), repr(t.value[0]), str(t.lexpos))
    print(estado)
    resultado_lexema.append(estado)
    t.lexer.skip(1)

t_ignore = ' \t'  # Ignorar espacios en blanco y tabulaciones



def t_error(t):
    global resultado_lexema
    if isinstance(t, LexError):
        estado = f"Error de análisis léxico: {t}"
        print(estado)
        resultado_lexema.append(estado)
    else:
        estado = "** TOKEN NO VALIDO EN LA LINEA: {:4} Valor: {:16} Posición: {:4}".format(str(t.lineno), str(t.value), str(t.lexpos))
        print(estado)
        if resultado_lexema:  # Verifica si la lista no está vacía antes de hacer pop
            resultado_lexema.pop()
        resultado_lexema.append(estado)
    t.lexer.skip(1)


# Prueba de ingreso
def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    tokens = []
    for token in analizador:
        tokens.append(token)
        if len(tokens) < 2:
            continue
        prev_token = tokens[-2]
        if prev_token.type == 'var':
            var_name = token.value
            if var_name in reservada:
                token.type = var_name
        estado = "Línea: {:4} ----Token: {:16} ----Lexema: {:16} ----Posición: {:4}".format(str(token.lineno),str(token.type) ,str(token.value), str(token.lexpos))
        resultado_lexema.append(estado)
    return tokens


# Instanciamos el analizador léxico
analizador = lex.lex()

if __name__ == '__main__':
    while True:
        data = input("Ingrese: ")
        prueba(data)
        print(resultado_lexema)