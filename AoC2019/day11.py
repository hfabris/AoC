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

def rotate(direction, facing,x,y):
    if facing == 1:      
        x -= 1
        facing = -2
    elif facing == -1: 
        x += 1
        facing = 2
    elif facing == -2:  
        y -= 1
        facing = -1
    elif facing == 2: 
        y += 1
        facing = 1
    return facing,x,y

def run():
    x,y = 0,0
    position = 0
    base = 0
    painted = []
    facing = 1
    value = True
    colour[(x,y)] = 1
    
    xmin, xmax = 0,0
    ymin, ymax = 0,0
    
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
            second = colour.get( (x,y), 0)
            put_result(dict.get(position+1,0), param1, base, int(second))
            position += 2
            
        elif( opcode == 4):
            if value:
                value = False
                if ((x,y)) not in painted:
                    painted.append( (x,y) )
                    if x < xmin: xmin = x
                    elif x > xmax: xmax = x
                    if y < ymin: ymin = y
                    elif y > ymax: ymax = y
                colour[(x,y)] = first
            else:
                value = True
                if first == 0:  facing,x,y = rotate(first, facing, x, y) 
                else :  facing,x,y = rotate(first, -1 * facing, x, y) 
            
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
    print( len(painted))    
    
    for j in range(ymin, ymax+1):
        line = ""
        for i in range(xmin,xmax+1):
           col = colour.get((i,j), 0)
           if col == 0: line += "  "
           else: line += "##"
        print( line)

file = open(sys.argv[1],'r')

file = list(map( int, file.readline().split(",")))
numbers = file.copy()

dict = {}
colour = {}

for i in range(len(numbers)):
    dict[i] = numbers[i]


run()

