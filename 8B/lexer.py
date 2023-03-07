import ply.lex as lex

tokens = (
    'NUMERO',
    'MAS',
    'MENOS',
    'POR',
    'ENTRE',
    'ID',
    'IGUAL',
    'DELIMITADOR',
    'MENOR',
    'MAYOR',
    
)
reserved = {
    'TNI' : 'int', 
    'TAOLF' : 'float',
    'FI' : 'if',
    'ESLE' : 'else',
    'ELIHW': 'while',
    'ROF' : 'for',
    'NAELOOB' : 'boolean',
    'MAS' : 'SUMA',
    'MENOS' : 'RESTA',
    'POR' : 'MULTIPLICACION',
    'ENTRE' : 'DIVISION',
    'DIF' : 'DIFERENCIA',
    'MENOR' : 'MenorA',
    'MAYOR' : 'MayorA'
}


tokens = list(tokens) + list(reserved.values())

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_] [a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t  

t_MAS = r'SUMA'
t_MENOS = r'RESTA'

t_POR = r'\*'
t_ENTRE = r'/'
t_IGUAL = r'::' 
t_DELIMITADOR = r';'
t_DIFERENCIA = r'DIF'
t_MENOR = 'MENOR'
t_MAYOR = 'MAYOR'

t_float = 'TAOLF'
t_if = 'FI'
t_else = 'ESLE'
t_while = 'ELIHW'
t_for = 'ROF'
t_boolean = 'NAELOOB'


t_ignore = ' \t\n'


lexer = lex.lex()

def t_ERROR(t):
    print("Token desconocido: '%s'" % t.value[0])
    t.lexer.skip(1)

with open('8B/data.txt', 'r') as file:  
    data = file.read()
    lexer.input(data)
    
while(True):
    tok = lexer.token()
    if not tok:
        break
    print(tok)