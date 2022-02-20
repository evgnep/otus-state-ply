import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lex import tokens

# expression : expression PLUS expression
#            | expression MINUS expression
#            | expression TIMES expression
#            | expression DIVIDE expression
#            | LPAREN expression RPAREN
#            | NUMBER


def p_plus(p):
    'expression : expression PLUS expression'
    p[0] = p[1] + p[3]


def p_minus(p):
    'expression : expression MINUS expression'
    p[0] = p[1] - p[3]


def p_times(p):
    'expression : expression TIMES expression'
    p[0] = p[1] * p[3]


def p_div(p):
    'expression : expression DIVIDE expression'
    p[0] = p[1] / p[4]


def p_num(p):
    'expression : NUMBER'
    p[0] = p[1]


def p_paren(p):
    'expression : LPAREN NUMBER RPAREN'
    p[0] = p[2]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


#precedence = (
#     ('left', 'PLUS', 'MINUS'),
#     ('left', 'TIMES', 'DIVIDE'),
#)


# Build the parser
parser = yacc.yacc()

if __name__ == '__main__':
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s) #, debug=1)
        print(result)


