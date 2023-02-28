import ply.lex as lex

tokens = (
    'NUMERO',
    'SUMA',
    'RESTA',
    'MULTIPLICAR',
    'DIVISION',
    'ID',
)
reserved = {
    'if' :  'CONDICIONAL',
    'else': 'SINO',
    'then': 'ENTONCES',
    'while':'CICLO_MIENTRAS',
    'for':  'CICLO_PARA',
      
    
}

tokens = list(tokens) + list(reserved.values())
# Expresiones Regulares de reconocimiento
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_] [a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t  

t_SUMA = r'\+'
t_RESTA = r'-'  
t_MULTIPLICAR = r'\*' 
t_DIVISION = r'/'
t_CONDICIONAL = 'if'
t_SINO = 'else'

#t_ID = r'[a-zA-Z_][a-zA-Z0-9_]+' 

# Caracteres ignorados
t_ignore = ' \t\n'

# Manejo de Errores
lexer = lex.lex()
def t_ERROR(t):
    print("Token desconocido: '%s'" % t.value[0])
    t.lexer.skip(1)

with open('data.txt', 'r') as file:  #Con With creamos la instancia y una vez terminado destruye la instancia.
    data = file.read()
    lexer.input(data)
    
while(True):
    tok = lexer.token()
    if not tok:
        break
    print(tok)




