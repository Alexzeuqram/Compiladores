import ply.yacc as yacc
from lexer import tokens

'''
expresion = expresion + termino |
            expresion - termino |
            termino

termino : factor |
          NUMERO

factor :  NUMERO


'''
def p_expresion_MAS(p):
    'expresion : expresion MAS termino'
    #p[0] = p[1] + p[3]
    print('Expresión SUMA escrita de manera CORRECTA')
    
def p_expresion_MENOS(p):
    'expresion : expresion MENOS termino'
    p[0] = p[1] - p[3]

def p_expresion_ID(p):
    'expresion : termino'
    p[0] = p[1]

def p_termino_factor(p):
    'termino : factor'
    p[0] = p[1]

def p_factor_NUMERO(p):
    'factor : NUMERO'
    p[0] = p[1] 

def p_error(p):
    print('Error de Sintaxs')

parser = yacc.yacc()

while(True):
    try:
        entrada = input()
    except EOFError:
        break

    if entrada.__eq__('exit'): break
    if not entrada : continue

    resultado = parser.parse(entrada)
    print(resultado)
