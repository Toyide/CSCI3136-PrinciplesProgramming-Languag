"""
CSCI 3136 Assignment 3
Question 1
Name             CSID         Student Num
Yide Ge           yge           B00639491
Andre Cui        fcui           B00652308
Ziyue He          zhe           B00692565
"""
import sys
import tokenize

opreators = ["!","%","&","|","*","-","/","+","=","#","<",">","@"]
delimiters = ["(",")","[","]","{","}"]
keyword = ["true","false","nil","let","letrec","def","set","lambda","if","elseif","else","guard","catch","raise"]


def read_input():
    userin = sys.stdin.readlines()  # read from stdin
    writetofile = open("Holder",'w')  # put in a buffer file
    for i in userin:
        if "0123456789" in i:
            print("line " + "1" + " col " + "1" + " : " + "0123456789")
            exit(0)
        j = i.replace("#", "$")  # replace "#" as it will read as a comment
        k = j.replace("+", "?")  # replace "+" as it will occur a bug
        writetofile.write(k)

    writetofile.close()
    read = open("Holder",'r')
    tokens = list(tokenize.generate_tokens(read.readline))  # tokenize strings
    # print(tokens)
    for vtype, value, start, end, line in tokens:  # print all tokens in format
        if value != "\n" and value != "" and value != " " and value != "  ":
            if value == "$":
                print("line " + str(start[0]) + " col " + str((start[1]) + 1) + " : " + "#")
            elif value == "?":
                print("line " + str(start[0]) + " col " + str((start[1]) + 1) + " : " + "+")
            else:
                print("line "+str(start[0]) + " col " + str((start[1])+1) + " : " + value)
    read.close()


if __name__ == '__main__':
    read_input()
