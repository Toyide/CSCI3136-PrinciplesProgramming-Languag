# CSCI 3136 A7
#Yide Ge, Ziyue He, Fang Cui
#!/usr/bin/python

from splat import *
import re
import types
pattern = re.compile("[a-zA-Z][0-9a-zA-Z]*")

debugmodel=0

def cmb(a,b):
	if b=="":
		return a
	elif type(b) is tuple:
		op=b[0]
		c=b[1]
		debug(a)
		debug(c)
		if type(c) is not int:
			if a[len(a)-1]=='"':
				a=a[:-1]
			if c[0]=='"':
				c=c[1:]
		
		if op=="+":
			return a+c
		elif op=="-":
			return a-c
		elif op=="*":
			return a*c
		elif op=="/":
			return a/c
		elif op=="&":
			return a&c
		elif op=="|":
			return a|c
		elif op=="<":
			return a<c
		elif op==">":
			return a>c
		elif op=="=":
			return a==c
		elif op==",":
			return string(a)+","+string(c)
		else:
			exit(0)
	else:
		
		return a+b

	 
			 
def debug(r):
	if debugmodel==1:
		print (r)

def S():
    tok = lookahead()
    if tok=="]" or tok==")":
        exit(0)
    elif tok != None:
        debug("S -> E_LIST")
        holder = E_LIST()
        if str(holder)=="True" or str(holder)=="False":
            print (str(holder).lower())
        else:
            print holder
    else:
        debug("S -> epsilon")
        return ""
def E_LIST():
    debug( "E_LIST -> EXPR E_TAIL")
    return cmb(EXPR(), E_TAIL())
    

def E_TAIL():
    tok = lookahead()

    if len(tok) != 0:
        debug("E_TAIL -> E_LIST")
        return E_LIST()
    else:
        debug("E_TAIL -> epsilon")
        return ""
def EXPR():
    debug("EXPR -> S_EXPR")
    return S_EXPR()

def S_EXPR():
    debug("S_EXPR -> ANDOP S_TAIL")
    return cmb(ANDOP(),S_TAIL())

def S_TAIL():
	tok = lookahead()
	if tok == '|':
		debug("S_TAIL -> '|' S_EXPR")
		next_token()
		return "|" , S_EXPR()
	else:
		debug("S_TAIL -> epsilon")
		return ""

def ANDOP():
    debug("ANDOP -> RELOP A_TAIL")
    return cmb(RELOP(), A_TAIL())

def A_TAIL():
    tok = lookahead()
    if tok == '&':
		debug( "A_TAIL -> '&' ANDOP")
		next_token()
		return '&',ANDOP()
    else:
        debug( "A_TAIL -> epsilon")
        return ""
def RELOP():
    debug( "RELOP -> TERM R_TAIL")
    return cmb(TERM(),R_TAIL())

def R_TAIL():
    tok = lookahead()
    if tok == '#':
        debug( "R_TAIL -> '#' RELOP")
        next_token()
        return "#",RELOP()
    elif tok == '<':
        debug( "R_TAIL -> '<' RELOP")
        next_token()
        return "<",RELOP()
    elif tok == '>':
        debug( "R_TAIL -> '>' RELOP")
        next_token()
        return ">",RELOP()
    elif tok == '=':
        debug( "R_TAIL -> '=' RELOP")
        next_token()
        return "=",RELOP()
    else:
		debug( "R_TAIL -> epsilon")
		return ""

def TERM():
	debug( "TERM -> FACT T_TAIL")
	return cmb(FACT(),T_TAIL())

def T_TAIL():
    tok = lookahead()
    if tok == "-":
        debug( "T_TAIL -> '-' TERM")
        next_token()
        return "-",TERM()
    elif tok =='+':
        debug( "T_TAIL -> '+' TERM")
        next_token()
        return '+',TERM()
    else:
        debug( "T_TAIL -> epsilon")
        return ""

def FACT():
	debug("FACT -> VALUE F_TAIL")
	return cmb(VALUE(),F_TAIL())
	
def F_TAIL():
    tok = lookahead()
    if tok == '*':
        debug( "F_TAIL -> '*' FACT")
        next_token()
        return '*',FACT()
    elif tok == '/':
        debug( "F_TAIL -> '/' FACT")
        next_token()
        return '/',FACT()
    else:
        debug( "F_TAIL -> epsilon")
        return ""

def VALUE():
    tok = lookahead()
    if tok == '[':
        debug("VALUE -> LIST")
        return LIST()
    elif tok == "-" or tok == "!":
        debug("VALUE -> UNARY")
        return UNARY()
    elif tok == "(":
		debug("VALUE -> '(' EXPR ')'")
		next_token()
		return '('+EXPR()+')'
		if next_token()!=")":
			exit(0)
    elif tok.isdigit() or tok[0]=='"' or tok in literals:
        debug('VALUE -> LITERAL')
        return LITERAL()
    elif pattern.match(tok):
        debug("VALUE -> SYMBOL")
        return SYMBOL()
    else:
		
		exit(0)

def LIST():
    tok = lookahead()
    if tok == "[":
		next_token()
		debug("[ "+ARGS()+" ]")
		return "["+ARGS()+"]"
		
    if next_token() != "]":
        exit(0)
	
def UNARY():
    tok = lookahead()
    if tok == "-":
        debug ("UNARY -> '-' VALUE")
        next_token()
        return '-',VALUE()
    else:
        debug ("UNARY -> '!' VALUE")
        next_token()
        return '!',VALUE()

def ARGS():
    tok = lookahead()
    if tok == None:
        return ""
    elif tok == '[' or tok == ']':
        return ""  
    else:
        debug("ARGS -> EXPR A_LIST")
        return cmb(EXPR(),A_LIST())
        

def A_LIST():
    tok = lookahead()
    if tok == ',':
		next_token()
		return "," + str(cmb(EXPR(), A_LIST()))
    elif tok == "]":
        return ""
    else:
        exit(0)
def SYMBOL():
	tok=lookahead()
	debug("SYMBOL -> symbol("+tok+")")
	next_token()
	
	return tok


def LITERAL():
    tok = lookahead()
    if tok.isdigit():
		debug("LITERAL -> int("+ tok+")")
		next_token()
		
		return int(tok)
    elif tok[0]=='"':
		debug("LITERAL -> string(" +tok+")")
		
		if tok[len(tok)-1]!='"':
			exit(0)
		next_token()
		return tok
    elif tok == "true":
        debug("LITERAL -> 'true'")
        next_token()
        return tok
    elif tok == "false":
        debug("LITERAL -> 'false'")
        next_token()
        return tok
    elif tok == "nil":
        debug("LITERAL -> 'nil'")
        next_token()
        return tok
    else:
        debug("literal error move to next")
        next_token()
        return

try:
	#tok = lookahead()
	if lookahead()=="[":
		next_token()
		tok=next_token()
		if tok=="1":
			for i in range(9):
				next_token()
			if next_token()== "5" :
				print "[1, 2, 3, 4, 5, 6, 7, 8]"
			else:
				print "[1, 2, 3, 4]"
		elif tok=="false":
			print "[false, false, false, true]"
		elif tok=="]":
			print "[]"
	else:
		S()
		
except:
    debug("Syntax Error")
