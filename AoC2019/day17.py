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
    # lines = []
    line = ""
    
    part = 0
    fun = [65,44,67,44,65,44,66,44,65,44,67,44,66,44,67,44,66,44,65,10]
    A = [76,44,49,50,44,82,44,52,44,82,44,52,44,76,44,54,10]
    B = [76,44,53,44,53,44,76,44,54,44,82,44,52,10]
    C = [76,44,49,50,44,82,44,52,44,82,44,52,44,82,44,49,50,10]
    end = [121, 10]

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
            # second = input("Please give ID of a system: ")
            if part == 0:   next = fun[0]; del fun[0]
            elif part == 1: next = A[0]; del A[0]
            elif part == 2: next = B[0]; del B[0]
            elif part == 3: next = C[0]; del C[0]
            elif part == 4: next = end[0]; del end[0]
            if int(next) == 10: part += 1
            second = next
            put_result(dict.get(position+1,0), param1, base, int(second))
            position += 2
            
        elif( opcode == 4):   
            if first < 256:
                line += chr(first)  
            else: print("Part 2: ", first )
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
    return line

def check_position(x,y, lines, xmax, ymax):
    
    if x-1 >= 0 and lines[y][x-1] != "#": return False
    elif x+1 < xmax and lines[y][x+1] != "#": return False
    
    if y-1 >= 0 and lines[y-1][x] != "#": return False
    elif y+1 < ymax and lines[y+1][x] != "#": return False
    
    return True
    
    
file = open(sys.argv[1],'r')

file = list(map( int, file.readline().split(",")))
numbers = file.copy()

dict = {}

for i in range(len(numbers)):
    dict[i] = numbers[i]

grid = calculate()

y,x = 0,0

lines = grid.strip().split("\n")

y = len(lines)
x = len(lines[0])
sum = 0

for j in range(y):
    for i in range(x):
        if check_position(i,j,lines, x, y):
            lines[j] =lines[j][:i] + "O" + lines[j][i+1:]
            sum += j*i

print("\n".join(lines))

print("Part 1: ", sum )

numbers[0] = 2

dict = {}
for i in range(len(numbers)):
    dict[i] = numbers[i]

grid = calculate()
