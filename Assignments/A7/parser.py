from splat import *
import re
pattern = re.compile("[a-zA-Z][0-9a-zA-Z]*")

def S():
    tok = lookahead()
    if tok=="]" or tok==")":
        exit(0)
    elif tok != None:
        # print "S -> E_LIST"
        E_LIST()
    else:
        # print "S -> epsilon"
		return ""

def E_LIST():
    # print "E_LIST -> EXPR E_TAIL"
    EXPR()
    E_TAIL()

def E_TAIL():
    tok = lookahead()

    if len(tok) != 0:
        # print"E_TAIL -> E_LIST"
        E_LIST()
    else:
        # print"E_TAIL -> epsilon"
		return ""

def EXPR():
    # print"EXPR -> S_EXPR"
    S_EXPR()

def S_EXPR():
    # print"S_EXPR -> ANDOP S_TAIL"
    ANDOP()
    S_TAIL()

def S_TAIL():
    tok = lookahead()
    if tok == '|':
        # print"S_TAIL -> '|' S_EXPR"
        next_token()
        S_EXPR()
    else:
        # print"S_TAIL -> epsilon"

def ANDOP():
    # print"ANDOP -> RELOP A_TAIL"
    RELOP()
    A_TAIL()

def A_TAIL():
    tok = lookahead()
    if tok == '&':
        # print "A_TAIL -> '&' ANDOP"
        next_token()
        ANDOP()
    else:
        # print "A_TAIL -> epsilon"

def RELOP():
    # print "RELOP -> TERM R_TAIL"
    return TERM()+R_TAIL()

def R_TAIL():
    tok = lookahead()
    if tok == '#':
        # print "R_TAIL -> '#' RELOP"
        next_token()
        return "#"+RELOP()
    elif tok == '<':
        # print "R_TAIL -> '<' RELOP"
        next_token()
        return "<"+RELOP()
    elif tok == '>':
        # print "R_TAIL -> '>' RELOP"
        next_token()
        return >RELOP()
    elif tok == '=':
        # print "R_TAIL -> '=' RELOP"
        next_token()
        return "="+RELOP()
    else:
        # print "R_TAIL -> epsilon"
		return

def TERM():
    # print "TERM -> FACT T_TAIL"
    FACT()
    T_TAIL()

def T_TAIL():
    tok = lookahead()
    if tok == "-":
        # print "T_TAIL -> '-' TERM"
        next_token()
        return -TERM()
    elif tok =='+':
        # print "T_TAIL -> '+' TERM"
        next_token()
        return +TERM()
    else:
        # print "T_TAIL -> epsilon"

def FACT():
    # print "FACT -> VALUE F_TAIL"
    return VALUE()+F_TAIL()

def F_TAIL():
    tok = lookahead()
    if tok == '*':
        # print "F_TAIL -> '*' FACT"
        next_token()
        return * FACT()
    elif tok == '/':
        # print "F_TAIL -> '/' FACT"
        next_token()
        return * FACT()
    else:
        print "F_TAIL -> epsilon"

def VALUE():
    tok = lookahead()
    if tok == '[':
        # print("VALUE -> LIST")
        LIST()
    elif tok == "-" or tok == "!":
        # print("VALUE -> UNARY")
        UNARY()
    elif tok == "(":
        print("VALUE -> '(' EXPR ')'")
        next_token()
        EXPR()
        if next_token()!=")":
            exit(0)
    elif tok.isdigit() or tok[0]=='"' or tok in literals:
        print('VALUE -> LITERAL')
        LITERAL()
    elif pattern.match(tok):
        print("VALUE -> SYMBOL")
        SYMBOL()
    else:
        exit(0)

def LIST():
    tok = lookahead()
    if tok == "[":
		next_token()
        print("[ "+ARGS()+" ]")
        
		
        if next_token() != "]":
            exit(0)

def UNARY():
    tok = lookahead()
    if tok == "-":
        # print "UNARY -> '-' VALUE"
        next_token()
        VALUE()
    else:
        print "UNARY -> '!' VALUE"
        next_token()
        VALUE()

def ARGS():
    tok = lookahead()
    if tok == None:
        return ""
    elif tok == '[' or tok == ']':
        return ""  
    else:
        # print"ARGS -> EXPR A_LIST"
        EXPR()
        A_LIST()

def A_LIST():
    tok = lookahead()
    if tok == ',':
		next_token()
        return "," + EXPR() +A_LIST()
        
    elif tok == "]":
        return ""
    else:
        exit(0)
def SYMBOL():
    tok=lookahead()
    # print("SYMBOL -> symbol("+tok+")")
    next_token()
	return "("+tok+")"

def LITERAL():
    tok = lookahead()
    if tok.isdigit():
        # print("LITERAL -> int("+ tok+")")
        next_token()
		return tok
    elif tok[0]=='"':
        # print("LITERAL -> string(" +tok+")")
		
        if tok[len(tok)-1]!='"':
            exit(0)
        next_token()
		return tok
    elif tok == "true":
        print("LITERAL -> 'true'")
        next_token()
    elif tok == "false":
        print("LITERAL -> 'false'")
        next_token()
    elif tok == "nil":
        print("LITERAL -> 'nil'")
        next_token()
    else:
        print"literal error move to next"
        next_token()

try:
        #tok = lookahead()
        S()
except:
    print("Syntax Error")
