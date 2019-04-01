import ply.lex as lex

reserved = {
    'athag': 'MAIN',
    'isulod': 'READ',
    'kung': 'IF',
    'kung di': 'ELSE',

    'para': 'FOR',
    'samtang': 'WHILE',

    'ibalik': 'RETURN',

    'ipagwa': 'PRINT'
}

tokens = [
    'IDNAME',
    'INT',
    'FLOAT',
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
    'ASSIGN',
    'COLON',
    'COMMENT',

    'PLUS',
    'MINUS',
    'MUL',
    'DIV',
    'MOD',

    'AND',
    'OR',
    'NOT',

    'EQ',
    'LEQ',
    'NEQ',
    'GEQ',
    'GT',
    'LT',
] + list(reserved.values())
# Regular expression rules for simple tokens 
t_ASSIGN = 'kay'
t_OPENPAR = r'\('
t_CLOSEPAR = r'\)'
t_OPENCURLY = '{'
t_CLOSECURLY = '}'
t_OPENBRACE = r'\['
t_CLOSEBRACE = r'\]'
t_COLON = ':'
t_COMMA = ','
t_PLUS = r'\+'
t_MINUS = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_MOD = r'%'
t_EQ = 'angay sa'
t_NEQ = 'di angay sa'
t_GT = 'dako sa'
t_LT = 'gamay sa'
t_LEQ = 'angay gamay sa'
t_GEQ = 'angay dako sa'
t_AND = r'kag'
t_OR = r'ukon'
t_NOT = r'di'

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

def t_INTLIT(t):
    r''
    t.value = str(t.value).strip('\"')
    return t

def t_FLTLIT

def t_COMMENT(t):
    r'

def t_FLOAT(t):
    r'\d+\.\d+' 
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

lexer = lex.lex()