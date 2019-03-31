import ply.lex as lex

reserved = {
    'kung': 'IF',
    'kung di': 'ELSE',

    'para': 'FOR',
    'samtang': 'WHILE',

    'ibalik': 'RETURN',

    'ipagwa': 'PRINT',

    'kag': 'AND',
    'ukon': 'OR',
    'di': 'NOT',
}

tokens = [
    'KEYWORD',
    'STMT_END',
    'EQUALS',
    'IDENTIFIER',
    'NUM_INT',
    'NUM_FLOAT',
    'LPAREN',
    'RPAREN',
    'LBRACK',
    'RBRACK',
    'COMMA',
    'STRING',
    'NEWLINE',
    'LSQBRACK',
    'RSQBRACK',
    'COLON',

    'PLUS',
    'MINUS',
    'MUL',
    'DIV',
    'MOD',

    'BIT_AND',
    'BIT_OR',
    'BIT_NEG',

    'DOUBLE_PLUS',
    'DOUBLE_MINUS',

    # 'PLUS_EQ',
    # 'MINUS_EQ',
    # 'MUL_EQ',
    # 'DIV_EQ',
    # 'MOD_EQ',
    # 'EXP_EQ',


    'TRUE',
    'FALSE',

    'EQ',
    'NEQ',
    'GT',
    'GTE',
    'LT',
    'LTE',
] + list(reserved.values())

t_COMMA = ','
t_PLUS = r'\+'
t_MINUS = '-'
t_MUL = r'\*'
t_DIV = r'/'
t_MOD = '%'
t_STMT_END = ':'
t_EQUALS = 'kay'
t_COLON = ':'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACK = '{'
t_RBRACK = '}'
t_LSQBRACK = r'\['
t_RSQBRACK = r'\]'
t_EQ = 'angay'
t_NEQ = 'di angay'
t_GT = 'mas dako'
t_GTE = 'angay dako'
t_LT = 'mas gamay'
t_LTE = 'angay gamay'

# t_PLUS_EQ = r'\+='
# t_MINUS_EQ = r'-='
# t_MUL_EQ = r'\*='
# t_DIV_EQ = r'/='
# t_MOD_EQ = '%='
# t_EXP_EQ = '\*\*='

t_BIT_AND = r'kag'
t_BIT_OR = r'ukon'
t_BIT_NEG = r'di'

t_DOUBLE_PLUS = r'\+\+'
t_DOUBLE_MINUS = '--'


def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    t.lexer.linepos = 0
    pass


def t_TRUE(t):
    'tuod'
    t.value = True
    return t


def t_FALSE(t):
    'sala'
    t.value = False
    return t


def t_IDENTIFIER(t):
    r'[\$_a-zA-Z]\w*'

    t.type = reserved.get(t.value, t.type)

    return t


def t_NUM_FLOAT(t):
    r'waki' 
    t.value = float(t.value)
    return t


def t_NUM_INT(t):
    r'bilog'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'"(?:\\"|.)*?"'

    t.value = bytes(t.value.lstrip('"').rstrip('"'), "utf-8").decode("unicode_escape")

    return t

lexer = lex.lex()