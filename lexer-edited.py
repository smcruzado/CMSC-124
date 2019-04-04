import ply.lex as lex
import sys
reserved = {
    'athag': 'MAIN',
    'isulod': 'READ',
    'kung': 'IF',
    'kung di': 'ELSE',

    'para': 'FOR',
    'samtang': 'WHILE',

    'ibalik': 'RETURN',

    'ipagwa': 'PRINT',
    'kay'   : 'ASSIGN',
    'bilog' : 'INT',
    'waki'  : 'FLOAT',
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

tokens = [
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

   
] + list(reserved.values())
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
def t_IDNAME(t):
    r'[a-z][a-zA-Z_0-9]*'
    # Check for reserved words
    t.type = reserved.get(t.value.lower(), 'IDNAME')
    return t

# Ignore whitespaces
t_ignore = ' \t'

def t_STRLIT(t):
    r'[\"][^\"]+[\"]'
    t.value = str(t.value).strip('\"')
    return t

def t_FLTLIT(t):
    r'\d+\.\d+' 
    t.value = float(t.value)
    return t

def t_INTLIT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_COMMENT(t):
    r'\//.*'
    pass
# Error handling rule
def t_error(t):
    print("SYNTAX ERROR: Illegal character: '%s' \n\tLine number: %d" % (t.value[0], t.lineno))
    t.lexer.skip(1)

lexer = lex.lex()


lexer.input("bilog a kay angaysa 10.95"
            "a+10 kay b"
            " ipagwa b" "//hello")
print("TOKENS:")
while True:
    tok = lexer.token()
    if not tok: 
        break
    print("\t",tok)
