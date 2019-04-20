

import ply.yacc as yacc
stmt_list=[]
tokens =lexer.toxens

precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE', 'MOD'),
)

def p_main_grammar(t):
    'main_statement: MAIN STRLIT OPENPAR CLOSEPAR COLON statement'


def p_statement(t):
    'statement: PRINT OPENPAR STRLIT CLOSEPAR'

def p_statement_assign(t):
    'statement : IDNAME ASSIGN expression'

def p_statement_expr(t):
    'statement : expression'

def p_statement_if(t):
    'statement : if_statement'

def p_statement_if_stmt(p):
    'if_statement : IF OPENPAR boolean_expression CLOSEPAR statement'
    if (p[3]):
        p[0] = p[5]

def p_statement_print(t):
    'statement : PRINT OPENPAR expression CLOSEPAR'
    print(t[3])

def p_statement_print_string(t):
    'statement : PRINT OPENPAR STRINGLIT RPAREN'
    print(t[3])

def p_statement_print_var(t):
    'statement : IDNAME ASSIGN expression PRINT OPENPAR IDNAME CLOSEPAR'
    print(t[3])

def p_statement_print_var_string(t):
    'statement : IDNAME ASSIGN STRLIT PRINT OPENPAR IDNAME CLOSEPAR'
    print(t[3])

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_expression_boolean(p):
    'expression : boolean_expression'
    p[0] = p[1]

def p_expression_greater(p):
    'boolean_expression : expression GT term'
    p[0] = p[1] > p[3]

def p_expression_greater_eq(p):
    'boolean_expression : expression GEQ term'
    p[0] = p[1] >= p[3]

def p_expression_less(p):
    'boolean_expression : expression LT term'
    p[0] = p[1] < p[3]

def p_expression_less_eq(p):
    'boolean_expression : expression LEQ term'
    p[0] = p[1] <= p[3]

def p_expression_equal(p):
    'boolean_expression : expression EQ term'
    p[0] = p[1] == p[3]

def p_expression_not_equal(p):
    'boolean_expression : expression NEQ term'
    p[0] = p[1] != p[3]

def p_expression_and(p):
    'boolean_expression : expression AND term'
    p[0] = p[1] and p[3]

def p_expression_or(p):
    'boolean_expression : expression OR term'
    p[0] = p[1] or p[3]

def p_expression_not(p):
    'boolean_expression : NOT expression'
    p[0] = not p[1]

def p_term_times(p):
    'term : term MUL factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIV factor'
    p[0] = p[1] / p[3]

def p_term_string(p):
    'term : STRLIT'
    p[0] = p[1]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : INTLIT'
    p[0] = p[1]
