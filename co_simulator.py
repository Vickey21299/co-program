"""CO SIMULATOR
<PC (8 bits) ><space><R0 (16 bits)><space>....<R6 (16 bits)><space><FLAG (16 bits)>"""

import sys
#m_file = sys.stdin.read().splitlines()

f = open("test2.txt","r")
m_file = f.read().splitlines()

instruction ={"add":"10000",
        "sub":"10001",
        "mov":("10010","10011"),
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


ty_reg={"000":["R0",0], 
        "001":["R1",0], 
        "010":["R2",0], 
        "011":["R3",0], 
        "100":["R4",0], 
        "101":["R5",0], 
        "110":["R6",0]}
FLAGS={"111":["FLAGS",0]}


#Initiation program counter PC
PC = 0

count = 0

address_memo = dict()
address = dict()
count1 =0

#conversion of decimial to binary

def DecToBin8(b):
    binary_ = bin(b)[2:]
    bin_ = (8-len(binary_))*"0"+str(bin)
    return bin_

def DecToBin16(b):
    binary_ = bin(b)[2:]
    bin_ = (8-len(binary_))*"0"+str(bin)
    return bin_

#conversion of a binary to decimal
def BinToDec(n):
    bin_ = int(n, 2)
    return bin_

#Store memory address for every line
for i in m_file:
    adress_memo[count]=0
    count= count +1

#if instruction load, store, jump.... check conversion binary to deci, 
    
    if( i[:5] == "10100" or i[:5] == "10101" or i[:5] == "11111" or i[:5] == "01100" or i[:5] == "01101" or i[:5] == "01111"):
        dec = BinToDec8(i[8:])
        adress_memo[count]= dec
        count +=1


MEM = []
cycle = []
c_count = 0

#type A inst
#addition instruction
for i in m_file:
    MEM.append(PC)
    cycle.append(c_count)
    c_count+=1

    if (i[:5]== "10000"):
        ty_reg.get(i[7:10])[1] = ty_reg.get(i[10:13])[1]+ ty_reg(i[13:])[1]

                #Flag SET condition
        if (ty_reg.get(i[7:10])[1]>((2**16)-1)):
            binary=bin(ty_reg.i(i[7:10])[1])
            #removing first two bits '0b'
            binary=binary[2:]
            result=binary[len(binary)-16:]
            result1=int(result,2)
            ty_reg.get(i[7:10])[1]=result1
            FLAGS.get("111")[1]+=8
        

        print(DecToBin8(PC)+" "+DecToBin16(ty_reg.get("000")[1])+" "+DecToBin16(ty_reg.get("001")[1])+" "+DecToBin16(REG_ADD.get("010")[1])+" "
        +DecToBin16(ty_reg.get("011")[1])+" "+DecToBin16(ty_reg.get("100")[1])+" "+DecToBin16(ty_reg.get("101")[1])+" "
        +DecToBin16(ty_reg.get("110")[1])+" "+DecToBin16(FLAGS.get("111")[1]))

        
        PC = PC+1
        
    #subtraction instruction
    if (i[0:5]=="10001"):

        ty_reg.get(i[7:10])[1] = ty_reg.get(i[10:13])[1] - ty_reg.get(i[13:])[1]
        
        #Flag SET condition
        if(ty_reg.get(i[7:10])[1]<0):
            ty_reg.get(i[7:10])[1]=0    
            FLAGS.get("111")[1]+=8

        print(DecToBin8(PC)+" "+DecToBin16(ty_reg.get("000")[1])+" "+DecToBin16(ty_reg.get("001")[1])+" "+DecToBin16(ty_reg.get("010")[1])+" "
        +DecToBin16(ty_reg.get("011")[1])+" "+DecToBin16(ty_reg.get("100")[1])+" "+DecToBin16(ty_reg.get("101")[1])+" "
        +DecToBin16(ty_reg.get("110")[1])+" "+DecToBin16(FLAGS.get("111")[1]))

        
        PC = PC +1

    #mult instruction
    if (i[0:5]=="10110"):

        ty_reg.get(i[7:10])[1] = ty_reg.get(i[10:13])[1] * ty_reg.get(i[13:])[1]
        
        #Flag SET condition
        if (ty_reg.get(i[7:10])[1]>((2**16)-1)):
            binary=bin(ty_reg.get(i[7:10])[1])
            #removing first two bits '0b'
            binary=binary[2:]
            result=binary[len(binary)-16:]
            result1=int(result,2)
            ty_reg.get(line[7:10])[1]=result1
            FLAGS.get("111")[1]+=8

        print(DecToBin8(PC)+" "+DecToBin16(ty_reg.get("000")[1])+" "+DecToBin16(ty_reg.get("001")[1])+" "+DecToBin16(ty_reg.get("010")[1])+" "
        +DecToBin16(ty_reg.get("011")[1])+" "+DecToBin16(ty_reg.get("100")[1])+" "+DecToBin16(ty_reg.get("101")[1])+" "
        +DecToBin16(ty_reg.get("110")[1])+" "+DecToBin16(FLAGS.get("111")[1]))            

        
        PC=PC+1   

    # Bitwise XOR
    if (i[0:5]=="11010"):

        ty_reg.get(i[7:10])[1] = ty_reg.get(i[10:13])[1] ^ ty_reg.get(i[13:])[1]
        

        print(DecToBin8(PC)+" "+DecToBin16(ty_reg.get("000")[1])+" "+DecToBin16(ty_reg.get("001")[1])+" "+DecToBin16(ty_reg.get("010")[1])+" "
        +DecToBin16(ty_reg.get("011")[1])+" "+DecToBin16(ty_reg.get("100")[1])+" "+DecToBin16(DecToBin16.get("101")[1])+" "
        +DecToBin16(ty_reg.get("110")[1])+" "+DecToBin16(FLAGS.get("111")[1]))            

        
        PC = PC+1
        FLAGS.get("111")[1]=0
        
    # Bitwise OR
    if (i[0:5]=="11011"):

        ty_reg.get(i[7:10])[1] = ty_reg.get(line[10:13])[1] | ty_reg.get(line[13:])[1]
        

        print(DecToBin8(PC)+" "+DecToBin16(ty_reg.get("000")[1])+" "+DecToBin16(ty_reg.get("001")[1])+" "+DecToBin16(ty_reg.get("010")[1])+" "
        +DecToBin16(ty_reg.get("011")[1])+" "+DecToBin16(ty_reg.get("100")[1])+" "+DecToBin16(ty_reg.get("101")[1])+" "
        +DecToBin16(ty_reg.get("110")[1])+" "+DecToBin16(FLAGS.get("111")[1]))            

        
        PC = PC +1         
        FLAGS.get("111")[1]=0

    # Bitwise AND
    if (i[0:5]=="11100"):

        ty_reg.get(i[7:10])[1] = ty_reg.get(i[10:13])[1] & ty_reg.get(i[13:])[1]
        

        print(DecToBin8(PC)+" "+DecToBin16(ty_reg.get("000")[1])+" "+DecToBin16(ty_reg.get("001")[1])+" "+DecToBin16(ty_reg.get("010")[1])+" "
        +DecToBin16(ty_reg.get("011")[1])+" "+DecToBin16(ty_reg.get("100")[1])+" "+DecToBin16(ty_reg.get("101")[1])+" "
        +DecToBin16(ty_reg.get("110")[1])+" "+DecToBin16(FLAGS.get("111")[1]))            

        
        PC= PC +1
        FLAGS.get("111")[1]=0


    # Type B inst
    # Move Imm
    if (i[0:5]=="10010"):
        
        ty_reg.get(i[5:8])[1] = BinToDec(line[8:])
        

        print(DecToBin8(PC)+" "+DecToBin16(ty_reg.get("000")[1])+" "+DecToBin16(ty_reg.get("001")[1])+" "+DecToBin16(ty_reg.get("010")[1])+" "
        +DecToBin16(ty_reg.get("011")[1])+" "+DecToBin16(ty_reg.get("100")[1])+" "+DecToBin16(ty_reg.get("101")[1])+" "
        +DecToBin16(ty_reg.get("110")[1])+" "+DecToBin16(FLAGS.get("111")[1]))            

        
        PC+=1
        FLAGS.get("111")[1]=0

    # Right Shift
    if (i[0:5]=="11000"):
        imm = BinToDec(i[8:])
        reg = ty_reg.get(i[5:8])[1]
        temp = ( reg >> imm )
        
        ty_reg.get(i[5:8])[1] = temp

        print(DecToBin8(PC)+" "+DecToBin16(ty_reg.get("000")[1])+" "+DecToBin16(ty_reg.get("001")[1])+" "+DecToBin16(ty_reg.get("010")[1])+" "
        +DecToBin16(ty_reg.get("011")[1])+" "+DecToBin16(ty_reg.get("100")[1])+" "+DecToBin16(ty_reg.get("101")[1])+" "
        +DecToBin16(ty_reg.get("110")[1])+" "+DecToBin16(FLAGS.get("111")[1]))            

        
        PC+=1
        FLAGS.get("111")[1]=0
    
    # Left Shift 
    if (i[0:5]=="11001"):

        imm = BinToDec(i[8:])
        reg = ty_reg.get(i[5:8])[1]
        temp = ( reg << imm )
        
        ty_reg.get(i[5:8])[1] = temp

        print(DecToBin8(PC)+" "+DecToBin16(ty_reg.get("000")[1])+" "+DecToBin16(ty_reg.get("001")[1])+" "+DecToBin16(ty_reg.get("010")[1])+" "
        +DecToBin16(ty_reg.get("011")[1])+" "+DecToBin16(ty_reg.get("100")[1])+" "+DecToBin16(ty_reg.get("101")[1])+" "
        +DecToBin16(ty_reg.get("110")[1])+" "+DecToBin16(FLAGS.get("111")[1]))            


        
        PC+=1
        FLAGS.get("111")[1]=0

    
    # Type C
    # move reg
    if (i[0:5]=="10011"):
        
        if(i[13:] in ty_reg.keys()):
            ty_reg.get(i[10:13])[1] = ty_reg.get(i[13:])[1]
        
        if(i[13:] in ty_reg.keys()):  #******** 
            ty_reg.get(i[10:13])[1] = FLAGS.get(i[13:])[1]
        
        FLAGS.get("111")[1]=0

        print(DecToBin8(PC)+" "+DecToBin16(ty_reg.get("000")[1])+" "+DecToBin16(ty_reg.get("001")[1])+" "+DecToBin16(ty_reg.get("010")[1])+" "
        +DecToBin16(ty_reg.get("011")[1])+" "+DecToBin16(ty_reg.get("100")[1])+" "+DecToBin16(ty_reg.get("101")[1])+" "
        +DecToBin16(ty_reg.get("110")[1])+" "+DecToBin16(FLAGS.get("111")[1]))            

        PC+=1
  

    # Divide
    if (i[0:5]=="10111"):

        # ty_reg.get("000")
        # print(ty_reg.get("000")[1])
        # q -> qoutient r -> remainder 
        q, r = divmod(ty_reg.get(i[10:13])[1], ty_reg.get(line[13:])[1])

        ty_reg.get("000")[1] = q
        ty_reg.get("001")[1] = r

        

        print(DecToBin8(PC)+" "+DecToBin16(ty_reg.get("000")[1])+" "+DecToBin16(ty_reg.get("001")[1])+" "+DecToBin16(ty_reg.get("010")[1])+" "
        +DecToBin16(ty_reg.get("011")[1])+" "+DecToBin16(ty_reg.get("100")[1])+" "+DecToBin16(ty_reg.get("101")[1])+" "
        +DecToBin16(ty_reg.get("110")[1])+" "+DecToBin16(FLAGS.get("111")[1]))            

        
        PC+=1
        FLAGS.get("111")[1]=0

    # Bitwise NOT
    if (i[0:5]=="11101"):

        ty_reg.get(i[10:13])[1] = ~ty_reg.get(i[13:])[1]
        

        print(DecToBin8(PC)+" "+DecToBin16(ty_reg.get("000")[1])+" "+DecToBin16(ty_reg.get("001")[1])+" "+DecToBin16(ty_reg.get("010")[1])+" "
        +DecToBin16(ty_reg.get("011")[1])+" "+DecToBin16(ty_reg.get("100")[1])+" "+DecToBin16(ty_reg.get("101")[1])+" "
        +DecToBin16(ty_reg.get("110")[1])+" "+DecToBin16(FLAGS.get("111")[1]))            

        
        PC+=1
        FLAGS.get("111")[1]=0

    # compare
    if (i[0:5]=="11110"):

        # less than
        if (ty_reg.get(i[10:13])[1] < ty_reg.get(i[13:])[1] ):
            
            
            FLAGS.get("111")[1]=4
        
        
    
        # greater than
        if ( ty_reg.get(i[10:13])[1] > ty_reg.get(i[13:])[1] ):

            FLAGS.get("111")[1]=2

        # equal to
        if ( ty_reg.get(i[10:13])[1] == ty_reg.get(i[13:])[1] ):

            FLAGS.get("111")[1]=1


        print(DecToBin8(PC)+" "+DecToBin16(ty_reg.get("000")[1])+" "+DecToBin16(ty_reg.get("001")[1])+" "+DecToBin16(ty_reg.get("010")[1])+" "
        +DecToBin16(ty_reg.get("011")[1])+" "+DecToBin16(ty_reg.get("100")[1])+" "+DecToBin16(ty_reg.get("101")[1])+" "
        +DecToBin16(ty_reg.get("110")[1])+" "+DecToBin16(FLAGS.get("111")[1]))            

        
        PC+=1
    
  # Type D opcode(5) reg1(3) mem_Address(8)
    # Load
    if (i[0:5]=="10100"):
       

        ty_reg.get(i[5:8])[1] = address_memo.get(BinToDec(i[8:]))
        MEM.append(address_memo.get(BinToDec(i[8:])))
        cycle.append(c_count-1)
        
        print(DecToBin8(PC)+" "+DecToBin16(ty_reg.get("000")[1])+" "+DecToBin16(ty_reg.get("001")[1])+" "+DecToBin16(ty_reg.get("010")[1])+" "
        +DecToBin16(ty_reg.get("011")[1])+" "+DecToBin16(ty_reg.get("100")[1])+" "+DecToBin16(ty_reg.get("101")[1])+" "
        +DecToBin16(ty_reg.get("110")[1])+" "+DecToBin16(FLAGS.get("111")[1]))            

        
        PC+=1
        FLAGS.get("111")[1]=0

    # Store
    if (i[0:5]=="10101"):
        
        
        address_memo[BinToDec(i[8:])]=ty_reg.get(i[5:8])[1]
        #print(Bin8(PC))
        MEM.append(address_memo.get(BinToDec(i[8:])))
        cycle.append(c_count-1)
        
        print(DecToBin8(PC)+" "+DecToBin16(ty_reg.get("000")[1])+" "+DecToBin16(ty_reg.get("001")[1])+" "+DecToBin16(ty_reg.get("010")[1])+" "
        +DecToBin16(ty_reg.get("011")[1])+" "+DecToBin16(ty_reg.get("100")[1])+" "+DecToBin16(ty_reg.get("101")[1])+" "
        +DecToBin16(ty_reg.get("110")[1])+" "+DecToBin16(FLAGS.get("111")[1]))            

        
        PC+=1
        FLAGS.get("111")[1]=0

    #Type E
    #jump
    if(i[0:5]=="11111"):
        FLAGS.get("111")[1]=0
        
        print(DecToBin8(PC)+" "+DecToBin16(ty_reg.get("000")[1])+" "+DecToBin16(ty_reg.get("001")[1])+" "+DecToBin16(ty_reg.get("010")[1])+" "
        +DecToBin16(ty_reg.get("011")[1])+" "+DecToBin16(ty_reg.get("100")[1])+" "+DecToBin16(ty_reg.get("101")[1])+" "
        +DecToBin16(ty_reg.get("110")[1])+" "+DecToBin16(FLAGS.get("111")[1]))            

        PC=address_memo[BinToDec(i[8:])]
        

    # jump if less than
    if(i[0:5]=="01100"):
        dec = FLAGS.get("111")[1]
        FLAGS.get("111")[1]=0
        
        print(DecToBin8(PC)+" "+DecToBin16(ty_reg.get("000")[1])+" "+DecToBin16(ty_reg.get("001")[1])+" "+DecToBin16(ty_reg.get("010")[1])+" "
        +DecToBin16(ty_reg.get("011")[1])+" "+DecToBin16(ty_reg.get("100")[1])+" "+DecToBin16(ty_reg.get("101")[1])+" "
        +DecToBin16(ty_reg.get("110")[1])+" "+DecToBin16(FLAGS.get("111")[1]))            

        if(dec ==4):
            PC=PC=address_memo[BinToDec(i[8:])]
            
        else:
            PC = PC+1
               
    
    #jump if greater than
    if(i[0:5]=="01101"):
        dec = FLAGS.get("111")[1]
        FLAGS.get("111")[1]=0
        
        print(DecToBin8(PC)+" "+DecToBin16(ty_reg.get("000")[1])+" "+DecToBin16(ty_reg.get("001")[1])+" "+DecToBin16(ty_reg.get("010")[1])+" "
        +DecToBin16(ty_reg.get("011")[1])+" "+DecToBin16(ty_reg.get("100")[1])+" "+DecToBin16(ty_reg.get("101")[1])+" "
        +DecToBin16(ty_reg.get("110")[1])+" "+DecToBin16(FLAGS.get("111")[1]))            

        if(dec==2):
            PC=PC=address_memo[BinToDec(i[8:])]
        else:
            PC+=1

       

    # jump if equal
    if(i[0:5]=="01111"):
        dec = FLAGS.get("111")[1]
        FLAGS.get("111")[1]=0
        
        print(DecToBin8(PC)+" "+DecToBin16(ty_reg.get("000")[1])+" "+DecToBin16(ty_reg.get("001")[1])+" "+DecToBin16(ty_reg.get("010")[1])+" "
        +DecToBin16(ty_reg.get("011")[1])+" "+DecToBin16(ty_reg.get("100")[1])+" "+DecToBin16(ty_reg.get("101")[1])+" "
        +DecToBin16(ty_reg.get("110")[1])+" "+DecToBin16(FLAGS.get("111")[1]))            

        if(dec==1):
            PC=PC=address_memo[BinToDec(i[8:])]
        else:
            PC+=1
       
    
    # Type F 
    # halt
    if (i[0:5]=="01010"):

        print(DecToBin8(PC)+" "+DecToBin16(ty_reg.get("000")[1])+" "+DecToBin16(ty_reg.get("001")[1])+" "+DecToBin16(ty_reg.get("010")[1])+" "
        +DecToBin16(ty_reg.get("011")[1])+" "+DecToBin16(ty_reg.get("100")[1])+" "+DecToBin16(ty_reg.get("101")[1])+" "
        +DecToBin16(ty_reg.get("110")[1])+" "+DecToBin16(FLAGS.get("111")[1]))            
       

        break



#print the input code after the output of it.
for i in m_file:
    print(i)


#store memory address of each line
for i in m_file:
    address_memo[count1]=0
    count1+=1
# to store mem_addr of variables
for i in m_file:
    if(i[0:5]=="10100" or i[0:5]=="100101" or i[0:5]=="11111" or i[0:5]=="01100" or i[0:5]=="01101"
     or i[0:5]=="01111"):
        x=address_memo[BinToDec(i[8:])]
        
        # printing the variables after the code ends
        print(DecToBin16(b))
        count1+=1

# printing 16 '0's to complete 256 lines of the code
for j in range(256-count1):
    print("0"*16)




# Plotting the graph for the simulator
import numpy as np
from matplotlib import pyplot as mp

mp.scatter(np.array(cycle),np.array(MEM),marker="+")
mp.ylabel("MEMORY")
mp.xlabel("CYCLE")
mp.show()                        

