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
t_ASSIGN = r"kay"
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
t_EQ = r'\angay sa'
t_NEQ = r'\di angay sa'
t_GT = r'\dako sa'
t_LT = r'\gamay sa'
t_LEQ = r'\angay gamay sa'
t_GEQ = r'\angay dako sa'
t_AND = r'\kag'
t_OR = r'\ukon'
t_NOT = r'\di'

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

def t_FLOAT(t):
    r'\d+\.\d+' 
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("SYNTAX ERROR: Illegal character: '%s' \n\tLine number: %d" % (t.value[0], t.lineno))
    t.lexer.skip(1)

lexer = lex.lex()


lexer.input("(kung a kay b)")
print("TOKENS:")
while True:
    tok = lexer.token()
    if not tok: 
        break
    print("\t",tok)
print("\nEVALUATION:")