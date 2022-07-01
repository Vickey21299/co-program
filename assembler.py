import sys
message  = sys.stdin.read()
opcode ={"add":"10000",
        "sub":"10001",
        "mov":"10010",
        "mov":"10011",
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
print(k)
inster=extractDigits(k)
print(inster)
def Add(a,b,c):
    binary_list.append(opcode["add"]+"00"+ty_reg[a]+ty_reg[b]+ty_reg[c]) # type A format of register
    return binary_list
def sub(a,b,c):
    binary_list.append(opcode["sub"]+"00"+ty_reg[a]+ty_reg[b]+ty_reg[c]) # type A format of register
    return binary_list
flag = False
error_line = 0
error_msg = ''
binary_list=[]

last_var = False
##Number of variables declared
line_count = 0
for x in inster:
    if x==[]:
        line_count+=1
    if x[0] in opcode:
        # checking opcode is maching or not 
        if x[0]=="add":
            line_count+=1
            Add(x[1],x[2],x[3])
        if x[0]=="sub":
            line_count+=1
            sub(x[1],x[2],x[3])
        if x[0]=="mov"


             

