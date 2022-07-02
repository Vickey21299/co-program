# co project starting 
# group 
from operator import invert
import sys
message  = sys.stdin.read()
op ={"add":"10000",
        "sub":"10001",
        "mov":("10010",
        "10011"),
        "ld":"10100",
        "st":"10101",
        "mul":"10110",
        "div":"10111",
        "rs":"11000",
        "ls":"11001",
        "xor":"11010",
        "or":"11011",
        "and":"11100",
        "not":"11101",
        "cmp":"11110",
        "jmp":"11111",
        "jlt":"01100",
        "jgt":"01101",
        "je":"01111",
        "hlt":"01010"}
ty_reg={"R0":'000',
"R1" : '001',
"R2": '010',
"R3":'011',
"R4":'100',
"R5":'101',
"R6":'110',
"FLAGS":'111'
}
def extractDigits(k):
    res = []
    for el in k:
        sub = el.split()
        res.append(sub)
      
    return(res)
k=list(message.split("\n"))
inster=extractDigits(k)
def Add(a,b,c):
    binary_list.append(op["add"]+"00"+ty_reg[a]+ty_reg[b]+ty_reg[c]) # type A format of register
    return binary_list
def sub(a,b,c):
    binary_list.append(op["sub"]+"00"+ty_reg[a]+ty_reg[b]+ty_reg[c]) # type A format of register
    return binary_list
def movimm(a,b):
    Binary =bin(int(b[1:]))[2:]
    if(len(Binary)<8):
        Imm=str("0"*(8-len(Binary)))+Binary
        binary_list.append(op["mov"][0]+ty_reg[a]+Imm) # type B register
        return binary_list
    else:
        binary_list.append(op["mov"][0]+ty_reg[a]+Binary)
        return binary_list
def movreg(a,b):
    binary_list.append(op["mov"][1]+"00000" + ty_reg[a]+ty_reg[b]) # type C register
    return binary_list
def load(a,b):
    Binary =bin(b)[2:]
    if(len(Binary)<8):
        Imm=str("0"*(8-len(Binary))+Binary)
        binary_list.append(op["ld"]+ty_reg[a]+Imm) # type B register
        return binary_list
    else:
        binary_list.append(op["ld"]+ty_reg[a]+Binary)
        return binary_list
def store(a,b):
    Binary =bin(b)[2:]
    if(len(Binary)<8):
        Imm=str("0"*(8-len(Binary))+Binary)
        binary_list.append(op["st"]+ty_reg[a]+Imm) # type B register
        return binary_list
    else:
        binary_list.append(op["st"]+ty_reg[a]+Binary)
        return binary_list
def  multiply(a,b,c):
    binary_list.append(op["mul"]+"00"+ty_reg[a]+ty_reg[b]+ty_reg[c]) # type A format of register
    return binary_list
def divide(a,b):
    binary_list.append(op["div"]+"00000" + ty_reg[a]+ty_reg[b]) # type C register
    return binary_list
def Rightshift(a,b):
    Binary =bin(int(b[1:])[2:])
    if(len(Binary)<8):
        Imm=str("0"*(8-len(Binary))+Binary)
        binary_list.append(op["st"]+ty_reg[a]+Imm) # type B register
        return binary_list
def leftshift(a,b):
    Binary =bin(int(b[1:])[2:])
    if(len(Binary)<8):
        Imm=str("0"*(8-len(Binary))+Binary)
        binary_list.append(op["st"]+ty_reg[a]+Imm) # type B register
        return binary_list
def exclusive_or(a,b,c):
    binary_list.append(op["xor"]+"00"+ty_reg[a]+ty_reg[b]+ty_reg[c]) # type A format of register
    return binary_list
def Or(a,b,c):
    binary_list.append(op["or"]+"00"+ty_reg[a]+ty_reg[b]+ty_reg[c]) # type A format of register
    return binary_list
def And(a,b,c):
    binary_list.append(op["and"]+"00"+ty_reg[a]+ty_reg[b]+ty_reg[c]) # type A format of register
    return binary_list
def Invert(a,b):
    binary_list.append(op["not"]+"00000" + ty_reg[a]+ty_reg[b]) # type C register
    return binary_list
def campare(a,b):
    binary_list.append(op["cmp"]+"00000" + ty_reg[a]+ty_reg[b]) # type C register
    return binary_list
def uncontroljump(a):
    Binary =bin(a)[2:]
    if(len(Binary)<8):
        Imm=str("0"*(8-len(Binary))+Binary)
        binary_list.append(op["jmp"]+"000"+Imm) # type E register
        return binary_list
def jumpless(a):
    Binary =bin(a)[2:]
    if(len(Binary)<8):
        Imm=str("0"*(8-len(Binary))+Binary)
        binary_list.append(op["jmp"]+"000"+Imm) # type E register
        return binary_list
def jumphigh(a):
    Binary =bin(a)[2:]
    if(len(Binary)<8):
        Imm=str("0"*(8-len(Binary))+Binary)
        binary_list.append(op["jmp"]+"000"+Imm) # type E register
        return binary_list
def jumpequal(a):
    Binary =bin(a)[2:]
    if(len(Binary)<8):
        Imm=str("0"*(8-len(Binary))+Binary)
        binary_list.append(op["jmp"]+"000"+Imm) # type E register
        return binary_list 
def Halt():
    binary_list.append(op["hlt"]+"00000000000")
    return binary_list

binary_list=[]
line_count = 0
for x in inster:
    if x==[]:
        line_count+=1
    if x!=[] and x[0] in op:
        # checking opcode  is maching or not 
        if x[0]=="add":
            line_count+=1
            Add(x[1],x[2],x[3])
        if x[0]=="sub":
            line_count+=1
            sub(x[1],x[2],x[3])
        if x[0]=="mov" and x[2][0]=='$':
            line_count+=1
            movimm(x[1],x[2])
        if x[0]=="mov" and x[2] in ty_reg:
            line_count+=1
            movreg(x[1],x[2])
        if x[0]=="ld":
            line_count+=1
            load(x[1],x[2])
        if x[0]=="st":
            line_count+=1
            store(x[1],x[2])
        if x[0]=="mul":
            line_count+=1
            multiply(x[1],x[2],x[3])
        if x[0]=="div":
            line_count+=1
            divide(x[1],x[2],x[3])
        if x[0]=="rs":
            line_count+=1
            Rightshift(x[1],x[2])
        if x[0]=="lf":
            line_count+=1
            leftshift(x[1],x[2])
        if x[0]=="xor":
            line_count+=1
            exclusive_or(x[1],x[2],x[3])
        if x[0]=="or":
            line_count+=1
            Or(x[1],x[2],x[3])
        if x[0]=="and":
            line_count+=1
            And(x[1],x[2],x[3])
        if x[0]=="not":
            line_count+=1
            invert(x[1],x[2])
        if x[0]=="cmp":
            line_count+=1
            campare(x[1],x[2],x[3])
        if x[0]=="jmp":
            line_count+=1
            uncontroljump(x[1])
        if x[0]=="jlt":
            line_count+=1
            jumpless(x[1])

        if x[0]=="jgt":
            line_count+=1
            jumphigh(x[1],x[2],x[3])
        if x[0]=="je":
            line_count+=1
            jumpequal(x[1],x[2],x[3])
        if x[0]=="hlt":
            line_count+=1
            Halt()
print(binary_list)      
        

