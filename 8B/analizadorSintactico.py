import ply.yacc as yacc
from lexer import tokens

'''
expresion = expresion + termino |
            expresion - termino |
            termino

termino : factor |
          NUMERO

factor :  NUMERO

declaracion : int + ID + IGUAL + termino 


'''
def p_expresion_SUMA(p):
    'expresion : expresion SUMA termino'
    p[0] = p[1] + p[3]
    print('Expresión SUMA escrita de manera CORRECTA')
    
def p_expresion_RESTA(p):
    'expresion : expresion RESTA termino'
    p[0] = p[1] - p[3]
    print('Expresion Resta escrita de manera correcta')

def p_expresion_DIVISION(p):
    'expresion : expresion DIVISION termino'
    p[0] = p[1] / p[3]
    print('Expresion division escrita de manera correcta')

def p_expresion_MULTIPLICACION(p):
    'expresion : expresion MULTIPLICACION termino'
    p[0] = p[1] * p[3]
    print('Expresion multiplicacion escrita de manera correcta')

def p_declaracion_INT(p):
    'expresion : int VARIABLE IGUAL termino DELIMITADOR'
    print('Declaracion de variable int escrita de manera correcta')

def p_declaracion_FLOAT(p):
    'expresion : float VARIABLE IGUAL termino DELIMITADOR'
    print('Declaracion de variable float escrita de manera correcta')

def p_declaracion_BOOLEAN_T(p):
    'expresion : boolean VARIABLE IGUAL bandera_T DELIMITADOR'
    print('Declaracion de variable boolean TRUE escrita de manera correcta')

def p_declaracion_BOOLEAN_F(p):
    'expresion : boolean VARIABLE IGUAL bandera_F DELIMITADOR'
    print('Declaracion de variable boolean FALSE escrita de manera correcta')

def p_concidional_IF_IGUAL(p):
    'expresion : if PARENTESIS_IZQ VARIABLE IGUAL IGUAL termino PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de condicional if IGUAL escrita de manera correcta')

def p_condicional_IF_IGUAL_MAYOR(p):
    'expresion : if PARENTESIS_IZQ VARIABLE  MayorA IGUAL termino PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de condicional if MAYOR IGUAL escrita de manera correcta')

def p_condicional_IF_IGUAL_MENOR(p):
    'expresion : if PARENTESIS_IZQ VARIABLE  MenorA IGUAL termino PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de condicional if MENOR IGUAL escrita de manera correcta')

def p_condicional_IF_DIFERENTE_A(p):
    'expresion : if PARENTESIS_IZQ VARIABLE  DIFERENCIA termino PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de condicional if DIFERENTE A escrita de manera correcta')

def p_condicional_IF_IGUAL_VAR(p):
    'expresion : if PARENTESIS_IZQ VARIABLE IGUAL IGUAL VARIABLE PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de condicional if IGUAL con VARIABLE escrita de manera correcta')

def p_condicional_IF_IGUAL_MAYOR_VAR(p):
    'expresion : if PARENTESIS_IZQ VARIABLE  MayorA IGUAL VARIABLE PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de condicional if MAYOR IGUAL con VARIABLE escrita de manera correcta')

def p_condicional_IF_IGUAL_MENOR_VAR(p):
    'expresion : if PARENTESIS_IZQ VARIABLE  MenorA IGUAL VARIABLE PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de condicional if MENOR IGUAL con VARIABLE escrita de manera correcta')

def p_condicional_IF_DIFERENTE_A_VAR(p):
    'expresion : if PARENTESIS_IZQ VARIABLE  DIFERENCIA VARIABLE PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de condicional if DIFERENTE A con VARIABLE escrita de manera correcta')

def p_condicional_IF_MAYOR(p):
    'expresion : if PARENTESIS_IZQ VARIABLE  MayorA  termino PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de condicional if MAYOR A escrita de manera correcta')

def p_condicional_IF_MENOR(p):
    'expresion : if PARENTESIS_IZQ VARIABLE  MenorA  termino PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de condicional if MENOR A escrita de manera correcta')

def p_condicional_IF_MENOR_ELSE(p):
    'expresion : if PARENTESIS_IZQ VARIABLE  MenorA  termino PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER else CORCHETE_IZQ CORCHETE_DER '
    print('Declaracion de condicional if ELSE MENOR A escrita de manera correcta')

def p_condicional_IF_IGUAL_ELSE(p):
    'expresion : if PARENTESIS_IZQ VARIABLE IGUAL IGUAL termino PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER else CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de condicional if ELSE IGUAL escrita de manera correcta')

def p_condicional_IF_IGUAL_MAYOR_ELSE(p):
    'expresion : if PARENTESIS_IZQ VARIABLE  MayorA IGUAL termino PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER else CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de condicional if ELSE IGUAL MAYOR A escrita de manera correcta')

def p_expresion_DECLARACION_IF_IGUAL_MENOR_ELSE(p):
    'expresion : if PARENTESIS_IZQ VARIABLE  MenorA IGUAL termino PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER else CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de condicional if ELSE IGUAL MENOR A escrita de manera correcta')

def p_expresion_DECLARACION_IF_DIFERENTE_A_ELSE(p):
    'expresion : if PARENTESIS_IZQ VARIABLE  DIFERENCIA termino PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER else CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de condicional if ELSE DIFERENTE A escrita de manera correcta')

def p_expresion_DECLARACION_IF_IGUAL_IGUAL_VAR_ELSE(p):
    'expresion : if PARENTESIS_IZQ VARIABLE IGUAL IGUAL VARIABLE PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER else CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de condicional if ELSE IGUAL A con VARIABLE escrita de manera correcta')

def p_expresion_DECLARACION_IF_IGUAL_MAYOR_VAR_ELSE(p):
    'expresion : if PARENTESIS_IZQ VARIABLE  MayorA IGUAL VARIABLE PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER else CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de condicional if ELSE IGUAL MAYOR A con VARIABLE escrita de manera correcta')

def p_expresion_DECLARACION_IF_IGUAL_MENOR_VAR_ELSE(p):
    'expresion : if PARENTESIS_IZQ VARIABLE  MenorA IGUAL VARIABLE PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER else CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de condicional if ELSE IGUAL MENOR A con VARIABLE escrita de manera correcta')

def p_expresion_DECLARACION_IF_DIFERENTE_A_VAR_ELSE(p):
    'expresion : if PARENTESIS_IZQ VARIABLE  DIFERENCIA VARIABLE PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER else CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de condicional if ELSE  DIFERENCIA A con VARIABLE escrita de manera correcta')

def p_expresion_DECLARACION_IF_MAYOR_ELSE(p):
    'expresion : if PARENTESIS_IZQ VARIABLE  MayorA  termino PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER else CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de condicional if ELSE MAYOR A escrita de manera correcta')

def p_expresion_DECLARACION_FOR_MAYOR(p):
    'expresion : for PARENTESIS_IZQ int VARIABLE  IGUAL  termino DELIMITADOR VARIABLE MayorA termino DELIMITADOR VARIABLE INCREMENTO PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de ciclo for MAYOR A escrita de manera correcta')

def p_expresion_DECLARACION_FOR_MENOR(p):
    'expresion : for PARENTESIS_IZQ int VARIABLE  IGUAL  termino DELIMITADOR VARIABLE  MenorA termino DELIMITADOR VARIABLE INCREMENTO PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de ciclo for MENOR A escrita de manera correcta')

def p_expresion_DECLARACION_FOR_MENOR_IGUAL(p):
    'expresion : for PARENTESIS_IZQ int VARIABLE  IGUAL  termino DELIMITADOR VARIABLE IGUAL MenorA termino DELIMITADOR VARIABLE INCREMENTO PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de ciclo for MENOR IGUAL A escrita de manera correcta')

def p_expresion_DECLARACION_FOR_MAYOR_IGUAL(p):
    'expresion : for PARENTESIS_IZQ int VARIABLE  IGUAL  termino DELIMITADOR VARIABLE IGUAL MayorA termino DELIMITADOR VARIABLE INCREMENTO PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de ciclo for MAYOR IGUAL A escrita de manera correcta')

def p_expresion_DECLARACION_FOR_MAYOR_DIFERENCIA(p):
    'expresion : for PARENTESIS_IZQ int VARIABLE  IGUAL  termino DELIMITADOR VARIABLE DIFERENCIA termino DELIMITADOR VARIABLE INCREMENTO PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de ciclo for MAYOR DIFERENCIA A escrita de manera correcta')

def p_expresion_DECLARACION_WHILE_MENOR(p):
    'expresion : while PARENTESIS_IZQ VARIABLE  MenorA  termino PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de ciclo WHILE MENOR A escrita de manera correcta')

def p_expresion_DECLARACION_WHILE_MAYOR(p):
    'expresion : while PARENTESIS_IZQ VARIABLE  MayorA  termino PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de ciclo WHILE MAYOR A escrita de manera correcta')

def p_expresion_DECLARACION_DO_WHILE_MAYOR(p):
    'expresion : DO CORCHETE_IZQ CORCHETE_DER while PARENTESIS_IZQ VARIABLE  MayorA  termino PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER'
    print(' Declaracion de ciclo DO WHILE MAYOR A escrita de manera correcta')

def p_expresion_DECLARACION_DO_WHILE_MENOR(p):
    'expresion : DO CORCHETE_IZQ CORCHETE_DER while PARENTESIS_IZQ VARIABLE  MenorA  termino PARENTESIS_DER  CORCHETE_IZQ CORCHETE_DER'
    print('Declaracion de ciclo DO WHILE MENOR A escrita de manera correcta')



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
