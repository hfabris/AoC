import sys

def calculate(numbers):
    position = 0

    while( numbers[position] != 99):
        opcode = numbers[position]
        first = numbers[numbers[position + 1]]
        second = numbers[numbers[position + 2]]
        result = numbers[position + 3]
    
        if( result > len(numbers)): break
        
        if( opcode == 1):
            numbers[result] = first + second
        elif( opcode == 2):
            numbers[result] = first * second
        else: break
    
        position += 4
    return numbers

input = open(sys.argv[1],'r')

input = list(map( int, input.readline().split(",")))
numbers = input.copy()

program = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,19,5,23,2,6,23,27,1,6,27,31,2,31,9,35,1,35,6,39,1,10,39,43,2,9,43,47,1,5,47,51,2,51,6,55,1,5,55,59,2,13,59,63,1,63,5,67,2,67,13,71,1,71,9,75,1,75,6,79,2,79,6,83,1,83,5,87,2,87,9,91,2,9,91,95,1,5,95,99,2,99,13,103,1,103,5,107,1,2,107,111,1,111,5,0,99,2,14,0,0]

print(calculate(program)[0])
print( calculate(numbers)[0])


for noun in range(1,100):
    for verb in range(1,100):
        numbers = input.copy()
        numbers[1] = noun
        numbers[2] = verb

        if( calculate(numbers)[0] == 19690720):
            print( "Noun, verb ", noun, verb)
            print( 100 * noun + verb)
            break
            
