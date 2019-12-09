import sys

def put_result(position, mode, base, result):
    if mode == 2:
        dict[base + position] = result
    else:
        dict[position] = result

def get_number( position, mode, base):
    if( mode == 0):
        return dict.get(dict.get(position,0),0)
    elif( mode == 1):
        return dict.get(position,0)
    elif( mode == 2):
        return dict.get(base+dict.get(position,0),0)
    else:   return False

def calculate():
    position = 0
    base = 0

    while( dict[position] != 99):
        opcode = dict[position] 
        if( position > len(dict)): break
        
        param1 = 0
        param2 = 0
        param3 = 0
        
        if( opcode > 10000):
            param3 = opcode // 10000
            param2 = (opcode // 1000) % 10
            param1 = (opcode // 100) % 10
            opcode = opcode % 100
        elif( opcode > 1000):
            param2 = opcode // 1000
            param1 = (opcode // 100) % 10
            opcode = opcode % 100
        elif( opcode > 100):
            param1 = opcode // 100
            opcode = opcode % 100
        
        first = get_number( position+1, param1, base)
        if( opcode not in [3,4,9]):
            second = get_number( position+2, param2, base)
        
        if( opcode == 1):
            put_result(dict.get(position+3, 0), param3, base, first+second)
            position += 4
            
        elif( opcode == 2):
            put_result(dict.get(position+3,0), param3, base, first*second)
            position += 4    
            
        elif( opcode == 3 ):
            first = dict[position + 1]
            second = input("Please give ID of a system: ")
            put_result(dict.get(position+1,0), param1, base, int(second))
            position += 2
            
        elif( opcode == 4):
            print( first )
            position += 2
            
        elif( opcode == 5):
            if( first != 0):
                position = second
            else:
                position += 3
                
        elif( opcode == 6):
            if( first == 0):
                position = second
            else:
                position += 3
                
        elif( opcode == 7):  
            if( first >= second):
                put_result(dict.get(position+3,0), param3, base, 0)
            else:
                put_result(dict.get(position+3,0), param3, base, 1)   
            position += 4
            
        elif( opcode == 8):
            if( first == second):
                put_result(dict.get(position+3,0), param3, base, 1)  
            else:
                put_result(dict.get(position+3,0), param3, base, 0)  
            position += 4
        elif( opcode == 9):
            base += first
            position += 2
        else: break


file = open(sys.argv[1],'r')

file = list(map( int, file.readline().split(",")))
numbers = file.copy()

dict = {}

for i in range(len(numbers)):
    dict[i] = numbers[i]

print("Part 1 input: 1\nPart 2 input: 2")

calculate()

