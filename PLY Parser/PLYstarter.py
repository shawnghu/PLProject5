tokens = ('INTEGER','STRING')
literals = ['.', ':' , '%', '+']

# Tokens

t_STRING = r'[(a-zA-Z]+[a-zA-Z\._/\-0-9:)\+]*'

def t_INTEGER(t):
    r'-?\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t\r\n"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex   # ply.lex comes from the ply folder in the PLY download.
lexer = lex.lex()

# Parsing rules

global time_step
time_step = 0

def p_start(t):
    '''start : header
             | data
             | empty
    '''
#    print "Saw :", t[1]

def p_header(t):
    'header : STRING STRING STRING STRING STRING STRING STRING STRING "%" STRING "%" STRING STRING STRING'
    print "Saw header"

def p_float(t):
    'float : INTEGER "." INTEGER'
    t[0] = str(t[1]) + str(t[2]) + str(t[3])

def p_data(t):
    '''data : INTEGER STRING STRING INTEGER INTEGER INTEGER INTEGER STRING float float INTEGER ":" float STRING
            | INTEGER STRING INTEGER INTEGER INTEGER INTEGER INTEGER STRING float float INTEGER ":" float STRING
    '''
    print "insert into toptb(pid, user, pr, ni, virt, res, shr, s, percpu, permem, plustime, command) values (",str(t[1]),", ",str(t[2]), ", ",str(t[3]), ", ", str(t[4]), ", ",str(t[5]),", ",str(t[6]), ", ",str(t[7]), ", ", str(t[8]), ", ",str(t[9]),", ",str(t[10]), ", ",str(t[11])+str(t[12])+str(t[13]), ", ", str(t[14]),")"

def p_empty(t):
    'empty : '
    pass

def p_error(t):
    if t == None:
        print("Syntax error at '%s'" % t)
    else:
        print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc   # ply.yacc comes from the ply folder in the PLY download.
parser = yacc.yacc()

while True:
    try:
        s = raw_input('')
    except EOFError:
        break
    parser.parse(s)

# To run the parser do the following in a terminal window: py | sed "s/_~_/ which is a float./"
