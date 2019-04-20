from ply import lex, yacc
import sys
#import ply.lex as lex
from ply.lex import TOKEN
import re
# List of tokens


reserved = {
    'athag': 'MAIN',
   # 'isulod': 'READ',
    #'kung': 'IF',
    #'kungdi': 'ELSE',

    #'para': 'FOR',
    #'samtang': 'WHILE',

    #'ibalik': 'RETURN',

    'ipagwa': 'PRINT',
    'kay'   : 'ASSIGN',
    'letra' : 'CHAR',
    'bilog' : 'INT',
    'waki'  : 'FLOAT',
    #'bool'  :  'BOOLEAN',
    'angaysa'  : 'EQ',
    'diangaysa'   : 'NEQ',
    'dakosa'   : 'GT',
    'gamaysa'  : 'LT',
    'angaygamaysa'  : 'LEQ',
    'angaydakosa' : 'GEQ',
    'kag'   : 'AND',
    'ukon'  : 'OR',
    'di'    : 'NOT',
}

tokens = (
    'IDNAME',
    'STRLIT',
    'INTLIT',
    'FLTLIT',
    
    
    'OPENBRACE',
    'CLOSEBRACE',
    'OPENPAR',
    'CLOSEPAR',
    'OPENCURLY',
    'CLOSECURLY',
    'COMMA',
    'COLON',
    'COMMENT',

    'PLUS',
    'MINUS',
    'MUL',
    'DIV',
    'MOD',

        )

tokens = list(reserved.values()) + list(tokens) 

# Regular expression rules for simple tokens
t_OPENPAR = r'\('
t_CLOSEPAR = r'\)'
t_OPENCURLY = r'{'
t_CLOSECURLY = r'}'
t_OPENBRACE = r'\['
t_CLOSEBRACE = r'\]'
t_COLON = r':'
t_COMMA = r','
t_PLUS = r'\+'
t_MINUS = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_MOD = r'%'


# Defining a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Determining if reserved word
#VAR
def t_IDNAME(t):
    r'[a-z][a-zA-Z_0-9]*'
    # Check for reserved words
    t.type = reserved.get(t.value.lower(), 'IDNAME')
    return t

# Ignore whitespaces
t_ignore = ' \t'

# RegExp for comments: No return value. Token discarded.
def t_COMMENT(t):
    r'\//.*'
    pass

def t_STRLIT(t):
        r'[\"][^\"]+[\"]'
        t.value = str(t.value).strip('\"')
        return t

def t_FLTLIT(t):
        r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'
        t.value = float(t.value)
        return t

def t_INTLIT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("SYNTAX ERROR: Illegal character: '%s' \n\tLine number: %d" % (t.value[0], t.lineno))
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# ---------------------------------------------end of lexer-------------------------------------------------------------
#import ply.yacc as yacc
precedence = (
    ('left','PLUS','MINUS'),
    ('left','MUL','DIV', 'MOD'),
)
t = lexer.token


def p_main_grammar(t):
    'statement : MAIN IDNAME OPENPAR CLOSEPAR COLON statement'

def p_statement(t):
    'statement : PRINT OPENPAR STRLIT CLOSEPAR'
    print (t[3])

def p_statement_assign_char(t):
    'statement : CHAR IDNAME statement'

def p_statement_expr(p):
    'statement : expression'
    print "Result =", p[1]

def p_statement_assign_int(t):
    'statement : INT IDNAME statement' 

def p_statement_assign_exxpr(t):
    'statement : IDNAME ASSIGN expression PRINT IDNAME'
    print(t[3])

def p_statement_assign_flt(t):
    'statement : FLOAT IDNAME IDNAME ASSIGN FLTLIT PRINT IDNAME'
    print(t[5]) 

def p_statement_express_int(p):
    'expression : INTLIT'
    p[0] = p[1]

def p_statement_express_flt(p):
    'expression : FLTLIT'
    p[0] = p[1]

def p_expression_plus(p):
    'expression : expression PLUS expression'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS expression'
    p[0] = p[1] - p[3]

def p_expression_mul(p):
    'expression : expression MUL expression'
    p[0] = p[1] * p[3]

def p_expression_div(p):
    'expression : expression DIV expression'
    p[0] = p[1] / p[3]

def p_expression_mod(p):
    'expression : expression MOD expression'
    p[0] = p[1] % p[3]

def p_expression_boolean(p):
    'expression : boolean_expression'
    p[0] = p[1]

def p_expression_lesser(p):
    'boolean_expression : INTLIT LT INTLIT'
    p[0] = p[1] < p[3]

def p_expression_greater(p):
    'boolean_expression : INTLIT GT INTLIT'
    p[0] = p[1] > p[3]

def p_expression_greater_eq(p):
    'boolean_expression : INTLIT GEQ INTLIT'
    p[0] = p[1] >= p[3]

def p_expression_less_eq(p):
    'boolean_expression : INTLIT LEQ INTLIT'
    p[0] = p[1] <= p[3]

def p_expression_equal(p):
    'boolean_expression : expression EQ expression'
    p[0] = p[1] == p[3]

def p_expression_not_equal(p):
    'boolean_expression : expression NEQ expression'
    p[0] = p[1] != p[3]

def p_expression_and(p):
    'boolean_expression : expression AND expression'
    p[0] = p[1] and p[3]

def p_expression_or(p):
    'boolean_expression : expression OR expression'
    p[0] = p[1] or p[3]

def p_expression_not(p):
    'boolean_expression : NOT expression'
    p[0] = not p[2]



def p_error(p):
     # print("Syntax Error")
     print("PARSER ERROR!: ",p)


parser = yacc.yacc()

# getting the file input from cmd
try:
    file_input = sys.argv[1];
    pass
except Exception as e:
    print("Missing file input!")
    print("Try this: python main.py <filename>")
    sys.exit()

# Open the input file.
f = open(file_input, 'r')
data = f.read()
f.close()

# Build the lexer
lexer.input(data)
print("TOKENS:")
while True:
    tok = lexer.token()
    if not tok: 
        break
    print("\t",tok)
print("\nEVALUATION:")

# while True:
#     try:
#         s = input('calc >')
#     except EOFError: break
yacc.yacc()
yacc.parse(data)
