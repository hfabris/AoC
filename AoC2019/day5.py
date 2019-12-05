import sys

def get_number(numbers, position, mode):
    if( mode == 0):
        return numbers[numbers[position]]
    elif( mode == 1):
        return numbers[position]
    else:   return False

def calculate(numbers):
    position = 0

    while( numbers[position] != 99):
        opcode = numbers[position] 
        if( position > len(numbers)): break
        
        param1 = 0
        param2 = 0
        
        
        if( opcode > 1000):
            param2 = opcode // 1000
            param1 = (opcode // 100) % 10
            opcode = opcode % 100
        elif( opcode > 100):
            param1 = opcode // 100
            opcode = opcode % 100
        
        
        first = get_number(numbers, position+1, param1)
        if( opcode != 3 and opcode != 4):
            second = get_number(numbers, position+2, param2)
        
        if( opcode == 1):
            result = numbers[position + 3]
            numbers[result] = first + second
            position += 4
            
        elif( opcode == 2):
            result = numbers[position + 3]        
            numbers[result] = first * second
            position += 4    
            
        elif( opcode == 3 ):
            first = numbers[position + 1]
            second = input("Please give ID of a system: ")
            numbers[first] = int(second)
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
                numbers[numbers[position+3]] = 0
            else:
                numbers[numbers[position+3]] = 1
            position += 4
            
        elif( opcode == 8):
            if( first == second):
                numbers[numbers[position+3]] = 1
            else:
                numbers[numbers[position+3]] = 0
            position += 4
        else: break


file = open(sys.argv[1],'r')

file = list(map( int, file.readline().split(",")))
numbers = file.copy()

calculate(numbers)

