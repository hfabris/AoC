import sys, numpy as np
from itertools import permutations

  
        
        
def get_number(numbers, position, mode):
    if( mode == 0):
        return numbers[numbers[position]]
    elif( mode == 1):
        return numbers[position]
    else:   return False

def calculate(numbers, phase, am_input, position):
    output = 0

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
            # second = input("Please give ID of a system: ")
            if position == 0: 
                numbers[first] = phase
            else:
                numbers[first] = am_input
            position += 2
            
        elif( opcode == 4):
            # print( first )
            output = first
             
            position += 2
            return(output, False, position)
            
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
    return(output, True, position)

def get_signal(iter):
    highest = 0

    for phase in permutations(iter):
        position = np.zeros(5, dtype=int)
        next = [0]
        done = False
        i = 0
   
        while not done:    
            out = calculate(numbers, phase[i], next[-1], position[i])
            position[i] = out[2]
            next.append(out[0])
            done = out[1]
            i = (i+1) % 5
        if next[-2] > highest:
            highest = next[-2]
        
    return highest


file = open(sys.argv[1],'r')

file = list(map( int, file.readline().split(",")))
numbers = file.copy()

machine_states = [[j for j in numbers] for _ in range(5)]

print( get_signal(range(5)))
print( get_signal(range(5,10)))
      
        
        
