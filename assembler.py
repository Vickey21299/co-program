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
num_var=0
binary_list=[]
count=0
line_count = 0
last_var=False
variables={}
lables={}
for x in inster:
    if (inster.index(x))+1==len(inster)-1 and ['hlt'] not in inster:
        error_message='hlt not present in line :' + str(len(inster))
        print(error_message)
        break
    elif x==['hlt'] and (inster.index(x))+1!= len(inster)-1:
        error_message ='hlt not in last instruction:'
        print(error_message)
        break
    elif ['hlt'] not in inster:
        error_message ='missing hlt or wrong syntax'
        print(error_message)
        break

    if x!=[] and x[0] in op:
        # checking opcode  is maching or not 
        if x[0]=="add":
            line_count+=1
            if len(x)!=4:
                error_message='Does Not Match the Required Number Of Tokens at line :' + str(inster.index(x)+1)
                print(error_message)
                break
                
            if x[1] not in ty_reg or x[2] not in ty_reg or x[3] not in ty_reg or "FLAGS" in x[1:]:
                error_message ="Invalid Register Name Used at line :" + str(inster.index(x)+1) 
                print(error_message)
                break
            Add(x[1],x[2],x[3])
        if x[0]=="sub":
            line_count+=1
            if len(x)!=4:
                error_message='Does Not Match the Required Number of token at line :' + str(inster.index(x)+1)
                print(error_message)
                break
            if x[1] not in ty_reg or x[2] not in ty_reg or x[3] not in ty_reg or "FLAGS" in x[1:]:
                error_message ="Invalid Register Name Used at line :" + str(inster.index(x)+1) 
                print(error_message)
                break
            sub(x[1],x[2],x[3])
        if x[0]=="mov" and x[2][0]=='$':
            line_count+=1
            if len(x)!=3:
                error_message='Does Not Match the Required Number of token at line :' + str(inster.index(x)+1)
                print(error_message)
                break
                
            if x[1] not in ty_reg  or "FLAGS" in x[1:]:
                error_message ="Invalid Register Name Used at line :" + str(inster.index(x)+1) 
                print(error_message)
                break
            if x[2][0] != "$" or not x[2][1:].isnumeric() or int(x[2][1:]) > 255 or int(x[2][1:]) < 0:
                error_message="Invalid Immediate Value Syntax at line : " + str(inster.index(x)+1)
                print(error_message)
                break
            movimm(x[1],x[2])
        if x[0]=="mov" and x[2] in ty_reg:
            line_count+=1
            if len(x)!=3:
                error_message='Does Not Match the Required Number of token at line :' + str(inster.index(x)+1)
                print(error_message)
                break
            if x[0] == 'mov':
                if x[1] not in ty_reg or x[1] == 'FLAGS' or x[2] not in ty_reg:
                    error_message= "Invalid register used at line : " + str(inster.index(x)+1)
                    print(error_message)
                    break
            if x[1] not in ty_reg  or x[2] not in ty_reg or "FLAGS" in x[1:]:
                error_message ="Invalid Register Name Used at line :" + str(inster.index(x)+1) 
                print(error_message)
                break
            movreg(x[1],x[2])
        if x[0]=="ld":
            line_count+=1
            if len(ith_instruction) != 3:
                error_message="Doesnot match the required number of tokens at line : " +  str(inster.index(x)+1)
                break
            if x[1] not in ty_reg or x[1] == "FLAGS":
                error_message="Invalid register name used at line : " +  str(inster.index(x)+1)
                break
            if x[2] not in variables:
                error_message="Variable Not Declared at line : " +  str(inster.index(x)+1)
                break
            load(x[1],variables[x[2]]+line_count+num_var)
        if x[0]=="st":
            line_count+=1
            if len(ith_instruction) != 3:
                error_message="Doesnot match the required number of tokens at line : " +  str(inster.index(x)+1)
                break
            if x[1] not in ty_reg or x[1] == "FLAGS":
                error_message="Invalid register name used at line : " +  str(inster.index(x)+1)
                break
            if x[2] not in variables:
                error_message="Variable Not Declared at line : " +  str(inster.index(x)+1)
                break
            store(x[1],variables[x[2]]+line_count + num_var)
        if x[0]=="mul":
            line_count+=1
            if len(x)!=4:
                error_message='Does Not Match the Required Number of token line :' + str(inster.index(x)+1)
                print(error_message)
                break
                
            if x[1] not in ty_reg or x[2] not in ty_reg or x[3] not in ty_reg or "FLAGS" in x[1:]:
                error_message ="Invalid Register Name Used at line :" + str(inster.index(x)+1) 
                print(error_message)
                break
            multiply(x[1],x[2],x[3])
        if x[0]=="div":
            line_count+=1
            if len(x)!=3:
                error_message='Does Not Match the Required Number of token at line :' + str(inster.index(x)+1)
                print(error_message)
                break
            if x[0] == 'mov':
                if x[1] not in ty_reg or x[1] == 'FLAGS' or x[2] not in ty_reg:
                    error_message= "Invalid register used at line : " + str(inster.index(x)+1)
                    print(error_message)
                    break
            if x[1] not in ty_reg  or x[2] not in ty_reg or "FLAGS" in x[1:]:
                error_message ="Invalid Register Name Used at line :" + str(inster.index(x)+1) 
                print(error_message)
                break
            divide(x[1],x[2],x[3])
        if x[0]=="rs":
            line_count+=1
            if len(x)!=3:
                error_message='Does Not Match the Required Number of token at line :' + str(inster.index(x)+1)
                print(error_message)
                break
                
            if x[1] not in ty_reg  or "FLAGS" in x[1:]:
                error_message ="Invalid Register Name Used at line :" + str(inster.index(x)+1) 
                print(error_message)
                break
            if x[2][0] != "$" or not x[2][1:].isnumeric() or int(x[2][1:]) > 255 or int(x[2][1:]) < 0:
                error_message="Invalid Immediate Value Syntax at line : " + str(inster.index(x)+1)
                print(error_message)
                break
            Rightshift(x[1],x[2])
        if x[0]=="lf":
            line_count+=1
            if len(x)!=3:
                error_message='Does Not Match the Required Number of token at line :' + str(inster.index(x)+1)
                print(error_message)
                break
                
            if x[1] not in ty_reg  or "FLAGS" in x[1:]:
                error_message ="Invalid Register Name Used at line :" + str(inster.index(x)+1) 
                print(error_message)
                break
            if x[2][0] != "$" or not x[2][1:].isnumeric() or int(x[2][1:]) > 255 or int(x[2][1:]) < 0:
                error_message="Invalid Immediate Value Syntax at line : " + str(inster.index(x)+1)
                print(error_message)
                break
            leftshift(x[1],x[2])
        if x[0]=="xor":
            line_count+=1
            if len(x)!=4:
                error_message='Does Not Match the Required Number of token at line :' + str(inster.index(x)+1)
                print(error_message)
                break
            if x[1] not in ty_reg or x[2] not in ty_reg or x[3] not in ty_reg or "FLAGS" in x[1:]:
                error_message ="Invalid Register Name Used at line :" + str(inster.index(x)+1) 
                print(error_message)
                break
            exclusive_or(x[1],x[2],x[3])
        if x[0]=="or":
            line_count+=1
            if len(x)!=4:
                error_message='Does Not Match the Required Number of token at line :' + str(inster.index(x)+1)
                print(error_message)
                break 
            if x[1] not in ty_reg or x[2] not in ty_reg or x[3] not in ty_reg or "FLAGS" in x[1:]:
                error_message ="Invalid Register Name Used at line :" + str(inster.index(x)+1) 
                print(error_message)
                break
            Or(x[1],x[2],x[3])
        if x[0]=="and":
            line_count+=1
            if len(x)!=4:
                error_message='Does Not Match the Required Number of token at line :' + str(inster.index(x)+1)
                print(error_message)
                break
            if x[1] not in ty_reg or x[2] not in ty_reg or x[3] not in ty_reg or "FLAGS" in x[1:]:
                error_message ="Invalid Register Name Used at line :" + str(inster.index(x)+1) 
                print(error_message)
                break
            And(x[1],x[2],x[3])
        if x[0]=="not":
            line_count+=1
            if len(x)!=3:
                error_message='Does Not Match the Required Number of token at line :' + str(inster.index(x)+1)
                print(error_message)
                break
            if x[0] == 'mov':
                if x[1] not in ty_reg or x[1] == 'FLAGS' or x[2] not in ty_reg:
                    error_message= "Invalid register used at line : " + str(inster.index(x)+1)
                    print(error_message)
                    break
            if x[1] not in ty_reg  or x[2] not in ty_reg or "FLAGS" in x[1:]:
                error_message ="Invalid Register Name Used at line :" + str(inster.index(x)+1) 
                print(error_message)
                break

            invert(x[1],x[2])
        if x[0]=="cmp":
            line_count+=1
            if len(x)!=3:
                error_message='Does Not Match the Required Number of token at line :' + str(inster.index(x)+1)
                print(error_message)
                break
            if x[0] == 'mov':
                if x[1] not in ty_reg or x[1] == 'FLAGS' or x[2] not in ty_reg:
                    error_message= "Invalid register used at line : " + str(inster.index(x)+1)
                    print(error_message)
                    break
            if x[1] not in ty_reg  or x[2] not in ty_reg or "FLAGS" in x[1:]:
                error_message ="Invalid Register Name Used at line :" + str(inster.index(x)+1) 
                print(error_message)
                break
            campare(x[1],x[2],x[3])
        if x[0]=="jmp":
            line_count+=1
            if len(x)!=2:
                error_message='Does Not Match the Required Number of token at line :' + str(inster.index(x)+1)
                print(error_message)
                break
            if x[1] not in lables:
                uncontroljump(inster.index[x]-num_var+1)
        if x[0]=="jlt":
            line_count+=1
            if len(x) != 2:
                error_message="Doesnot match the required number of tokens at line : " +  str(inster.index(x)+1)
                print(error_message)
                break
            if x[1] not in lables:
                error_message="Label Not Declared at line : " + str(inster.index(x)+1)
                print(error_message)
                break
            jumpless(inster.index[x]-num_var+1)
        if x[0]=="jgt":
            line_count+=1
            if len(x) != 2:
                error_message="Doesnot match the required number of tokens at line : " +  str(inster.index(x)+1)
                print(error_message)
                break
            if x[1] not in lables:
                error_message="Label Not Declared at line : " + str(inster.index(x)+1)
                print(error_message)
                break
            jumphigh(inster.index[x]-num_var+1)
        if x[0]=="je":
            line_count+=1
            if len(x) != 2:
                error_message="Doesnot match the required number of tokens at line : " +  str(inster.index(x)+1)
                print(error_message)
                break
            if x[1] not in lables:
                error_message="Label Not Declared at line : " + str(inster.index(x)+1)
                print(error_message)
                break
            jumpequal(inster.index[x]-num_var+1)
        if x[0]=="hlt":
            line_count+=1
            Halt()
    elif x!=[] and x[0]=="var": # check input as var 
        # if last_var:
        #     error_message='variable not declared at top :' + str(x[len(x)-1])
        #     print(error_message)
        #     break
        # if not num_var and x[inster.index(x)+1][0]!='var':
        #     last_var = True
        if len(x)!=2:
            error_message="wrong syntax for variable:" + str(x[len(x)-1])
            print(error_message)
            break
        ex = []      ##variable store
        ex.extend(x[1])
        for i in ex:
            if (ord(i) not in range(ord('a'), ord('z')+1)) :
                if (ord(i) not in range(ord('A'), ord('Z')+1)) :
                    if ord(i) != ord('_') and (ord(i) not in range(ord('0'), ord('9')+1)):
                        error_message = '  Wrong variable name line:: ' + str(x[len(x)-1])
                        print(error_message)
                        break
                    break
                break
            break

        if x[1] in variables:
            error_message = 'Error while declaring same variable again: ' + str(x[-1])
            print(error_message)
            break

        variables[x[1]] = inster.index(x)
        num_var += 1
        
        # lable declaration start
    elif  x!= [] and x[0][-1]==":":
        ex=[]
        ex.extend(x[1])
        for i in ex:
            if (ord(i) not in range(ord('a'), ord('z')+1)) :
                if (ord(i) not in range(ord('A'), ord('Z')+1)) :
                    if ord(i) != ord('_') and (ord(i) not in range(ord('0'), ord('9')+1)):
                        error_message = '  Wrong variable name line:: ' + str(x[len(x)-1])
                        print(error_message)
                        break
                    break
                break
            break
        if x[0][0:-1] in variables:
            error_message = 'Error while declaring same variable again: ' + str(x[-1])
            print(error_message)
            break
        # checking for lables start
        if x[1]==['hlt']:
            if len(x)!=2:
                error_message = 'wrong syntax at line'+str(len(inster)-1)
                print(error_message)
                break
            elif inster.index(x)!=len(inster)-1:
                error_message='hlt not in last line'
                print(error_message)
                break
            else:
                Halt()

        elif x!=[]and  x[1] in op:
            lable_name= x[0][0 :-1]
            x=x[1:]
            #starting all above code to re code starting with lable occurs
            if x[0]=="add":
                line_count+=1
                if len(x)!=4:
                    error_message='Does Not Match the Required Number Of Tokens at line :' + str(inster.index(x)+1)
                    print(error_message)
                    break
                    
                if x[1] not in ty_reg or x[2] not in ty_reg or x[3] not in ty_reg or "FLAGS" in x[1:]:
                    error_message ="Invalid Register Name Used at line :" + str(inster.index(x)+1) 
                    print(error_message)
                    break
                Add(x[1],x[2],x[3])
            if x[0]=="sub":
                line_count+=1
                if len(x)!=4:
                    error_message='Does Not Match the Required Number of token at line :' + str(inster.index(x)+1)
                    print(error_message)
                    break
                if x[1] not in ty_reg or x[2] not in ty_reg or x[3] not in ty_reg or "FLAGS" in x[1:]:
                    error_message ="Invalid Register Name Used at line :" + str(inster.index(x)+1) 
                    print(error_message)
                    break
                sub(x[1],x[2],x[3])
            if x[0]=="mov" and x[2][0]=='$':
                line_count+=1
                if len(x)!=3:
                    error_message='Does Not Match the Required Number of token at line :' + str(inster.index(x)+1)
                    print(error_message)
                    break
                    
                if x[1] not in ty_reg  or "FLAGS" in x[1:]:
                    error_message ="Invalid Register Name Used at line :" + str(inster.index(x)+1) 
                    print(error_message)
                    break
                if x[2][0] != "$" or not x[2][1:].isnumeric() or int(x[2][1:]) > 255 or int(x[2][1:]) < 0:
                    error_message="Invalid Immediate Value Syntax at line : " + str(inster.index(x)+1)
                    print(error_message)
                    break
                movimm(x[1],x[2])
            if x[0]=="mov" and x[2] in ty_reg:
                line_count+=1
                if len(x)!=3:
                    error_message='Does Not Match the Required Number of token at line :' + str(inster.index(x)+1)
                    print(error_message)
                    break
                if x[0] == 'mov':
                    if x[1] not in ty_reg or x[1] == 'FLAGS' or x[2] not in ty_reg:
                        error_message= "Invalid register used at line : " + str(inster.index(x)+1)
                        print(error_message)
                        break
                if x[1] not in ty_reg  or x[2] not in ty_reg or "FLAGS" in x[1:]:
                    error_message ="Invalid Register Name Used at line :" + str(inster.index(x)+1) 
                    print(error_message)
                    break
                movreg(x[1],x[2])
            if x[0]=="ld":
                line_count+=1
                if len(ith_instruction) != 3:
                    error_message="Doesnot match the required number of tokens at line : " +  str(inster.index(x)+1)
                    break
                if x[1] not in ty_reg or x[1] == "FLAGS":
                    error_message="Invalid register name used at line : " +  str(inster.index(x)+1)
                    break
                if x[2] not in variables:
                    error_message="Variable Not Declared at line : " +  str(inster.index(x)+1)
                    break
                load(x[1],variables[x[2]]+line_count+num_var)
            if x[0]=="st":
                line_count+=1
                if len(ith_instruction) != 3:
                    error_message="Doesnot match the required number of tokens at line : " +  str(inster.index(x)+1)
                    break
                if x[1] not in ty_reg or x[1] == "FLAGS":
                    error_message="Invalid register name used at line : " +  str(inster.index(x)+1)
                    break
                if x[2] not in variables:
                    error_message="Variable Not Declared at line : " +  str(inster.index(x)+1)
                    break
                store(x[1],variables[x[2]]+line_count + num_var)
            if x[0]=="mul":
                line_count+=1
                if len(x)!=4:
                    error_message='Does Not Match the Required Number of token line :' + str(inster.index(x)+1)
                    print(error_message)
                    break
                    
                if x[1] not in ty_reg or x[2] not in ty_reg or x[3] not in ty_reg or "FLAGS" in x[1:]:
                    error_message ="Invalid Register Name Used at line :" + str(inster.index(x)+1) 
                    print(error_message)
                    break
                multiply(x[1],x[2],x[3])
            if x[0]=="div":
                line_count+=1
                if len(x)!=3:
                    error_message='Does Not Match the Required Number of token at line :' + str(inster.index(x)+1)
                    print(error_message)
                    break
                if x[0] == 'mov':
                    if x[1] not in ty_reg or x[1] == 'FLAGS' or x[2] not in ty_reg:
                        error_message= "Invalid register used at line : " + str(inster.index(x)+1)
                        print(error_message)
                        break
                if x[1] not in ty_reg  or x[2] not in ty_reg or "FLAGS" in x[1:]:
                    error_message ="Invalid Register Name Used at line :" + str(inster.index(x)+1) 
                    print(error_message)
                    break
                divide(x[1],x[2],x[3])
            if x[0]=="rs":
                line_count+=1
                if len(x)!=3:
                    error_message='Does Not Match the Required Number of token at line :' + str(inster.index(x)+1)
                    print(error_message)
                    break
                    
                if x[1] not in ty_reg  or "FLAGS" in x[1:]:
                    error_message ="Invalid Register Name Used at line :" + str(inster.index(x)+1) 
                    print(error_message)
                    break
                if x[2][0] != "$" or not x[2][1:].isnumeric() or int(x[2][1:]) > 255 or int(x[2][1:]) < 0:
                    error_message="Invalid Immediate Value Syntax at line : " + str(inster.index(x)+1)
                    print(error_message)
                    break
                Rightshift(x[1],x[2])
            if x[0]=="lf":
                line_count+=1
                if len(x)!=3:
                    error_message='Does Not Match the Required Number of token at line :' + str(inster.index(x)+1)
                    print(error_message)
                    break
                    
                if x[1] not in ty_reg  or "FLAGS" in x[1:]:
                    error_message ="Invalid Register Name Used at line :" + str(inster.index(x)+1) 
                    print(error_message)
                    break
                if x[2][0] != "$" or not x[2][1:].isnumeric() or int(x[2][1:]) > 255 or int(x[2][1:]) < 0:
                    error_message="Invalid Immediate Value Syntax at line : " + str(inster.index(x)+1)
                    print(error_message)
                    break
                leftshift(x[1],x[2])
            if x[0]=="xor":
                line_count+=1
                if len(x)!=4:
                    error_message='Does Not Match the Required Number of token at line :' + str(inster.index(x)+1)
                    print(error_message)
                    break
                if x[1] not in ty_reg or x[2] not in ty_reg or x[3] not in ty_reg or "FLAGS" in x[1:]:
                    error_message ="Invalid Register Name Used at line :" + str(inster.index(x)+1) 
                    print(error_message)
                    break
                exclusive_or(x[1],x[2],x[3])
            if x[0]=="or":
                line_count+=1
                if len(x)!=4:
                    error_message='Does Not Match the Required Number of token at line :' + str(inster.index(x)+1)
                    print(error_message)
                    break 
                if x[1] not in ty_reg or x[2] not in ty_reg or x[3] not in ty_reg or "FLAGS" in x[1:]:
                    error_message ="Invalid Register Name Used at line :" + str(inster.index(x)+1) 
                    print(error_message)
                    break
                Or(x[1],x[2],x[3])
            if x[0]=="and":
                line_count+=1
                if len(x)!=4:
                    error_message='Does Not Match the Required Number of token at line :' + str(inster.index(x)+1)
                    print(error_message)
                    break
                if x[1] not in ty_reg or x[2] not in ty_reg or x[3] not in ty_reg or "FLAGS" in x[1:]:
                    error_message ="Invalid Register Name Used at line :" + str(inster.index(x)+1) 
                    print(error_message)
                    break
                And(x[1],x[2],x[3])
            if x[0]=="not":
                line_count+=1
                if len(x)!=3:
                    error_message='Does Not Match the Required Number of token at line :' + str(inster.index(x)+1)
                    print(error_message)
                    break
                if x[0] == 'mov':
                    if x[1] not in ty_reg or x[1] == 'FLAGS' or x[2] not in ty_reg:
                        error_message= "Invalid register used at line : " + str(inster.index(x)+1)
                        print(error_message)
                        break
                if x[1] not in ty_reg  or x[2] not in ty_reg or "FLAGS" in x[1:]:
                    error_message ="Invalid Register Name Used at line :" + str(inster.index(x)+1) 
                    print(error_message)
                    break

                invert(x[1],x[2])
            if x[0]=="cmp":
                line_count+=1
                if len(x)!=3:
                    error_message='Does Not Match the Required Number of token at line :' + str(inster.index(x)+1)
                    print(error_message)
                    break
                if x[0] == 'mov':
                    if x[1] not in ty_reg or x[1] == 'FLAGS' or x[2] not in ty_reg:
                        error_message= "Invalid register used at line : " + str(inster.index(x)+1)
                        print(error_message)
                        break
                if x[1] not in ty_reg  or x[2] not in ty_reg or "FLAGS" in x[1:]:
                    error_message ="Invalid Register Name Used at line :" + str(inster.index(x)+1) 
                    print(error_message)
                    break
                campare(x[1],x[2],x[3])
            if x[0]=="jmp":
                line_count+=1
                if len(x)!=2:
                    error_message='Does Not Match the Required Number of token at line :' + str(inster.index(x)+1)
                    print(error_message)
                    break
                if x[1] not in lables:
                    uncontroljump(inster.index[x]-num_var+1)
            if x[0]=="jlt":
                line_count+=1
                if len(x) != 2:
                    error_message="Doesnot match the required number of tokens at line : " +  str(inster.index(x)+1)
                    print(error_message)
                    break
                if x[1] not in lables:
                    error_message="Label Not Declared at line : " + str(inster.index(x)+1)
                    print(error_message)
                    break
                jumpless(inster.index[x]-num_var+1)
            if x[0]=="jgt":
                line_count+=1
                if len(x) != 2:
                    error_message="Doesnot match the required number of tokens at line : " +  str(inster.index(x)+1)
                    print(error_message)
                    break
                if x[1] not in lables:
                    error_message="Label Not Declared at line : " + str(inster.index(x)+1)
                    print(error_message)
                    break
                jumphigh(inster.index[x]-num_var+1)
            if x[0]=="je":
                line_count+=1
                if len(x) != 2:
                    error_message="Doesnot match the required number of tokens at line : " +  str(inster.index(x)+1)
                    print(error_message)
                    break
                if x[1] not in lables:
                    error_message="Label Not Declared at line : " + str(inster.index(x)+1)
                    print(error_message)
                    break
                jumpequal(inster.index[x]-num_var+1)
            if x[0]=="hlt":
                line_count+=1
                Halt()
            lables[lable_name]=inster.index(x)
        else:
            error_message="wrong command after lable"
            print(error_message)
            break
    else:
        error_message="syntax error on line:"+str(inster.index(x)+1)
        print(error_message)
   

for x in binary_list:
    print(x)      
        

