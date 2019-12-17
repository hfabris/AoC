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

def move(x,y,dir):
    # print( x,y,dir)
    if dir == 1: y -= 1
    elif dir == 2: y += 1
    elif dir == 3: x -= 1
    elif dir == 4: x += 1
    return x,y
    
def backtrace(x,y):
    x0,y0 = 0,0
    visited = []
    open = [ (x0,y0,0) ]
    while open:
        xc,yc,steps = open.pop()
        if xc == x and yc == y: 
            print(steps)
            return
        visited.append( (xc,yc) )
        for i in range(1,5):
            xn,yn = move(xc,yc,i)
            if (xn,yn) not in visited and map[(xn,yn)] == ".":
                open.append( (xn,yn,steps+1) )   

def print_map():
    map[ (0,0)] = "o"
    # print(map)
    k = map.keys()
    xmin,ymin = 0,0
    xmax,ymax = 0,0
    for x,y in k:
        if x < xmin: xmin = x
        elif x > xmax: xmax = x
        if y < ymin: ymin = y
        elif y > ymax: ymax = y
        
    for j in range(ymin, ymax+1):
        line = ""
        for i in range(xmin, xmax+1):
            line += map.get( (i,j), " ")
        print( line )

def get_back(x,y,xb,yb):
    if x != xb:
        if x < xb: return 4
        else: return 3
    if y != yb:
        if y < yb: return 2
        else: return 1
        
        
def calculate():
    position = 0
    base = 0
    reply = 1
    x,y = 0,0
    dir = 0
    backsteps = []
    dead = []
    direction = "forward"

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
            i = 0
            while True:
                i += 1
                if i > 4:
                    xb,yb = backsteps[-1]
                    del backsteps[-1]
                    # print(x,y,xb,yb)
                    i = get_back(x,y,xb,yb)
                    dead.append( (x,y) )
                    direction = "back"
                    x,y = xb,yb
                    second = i
                    dir = i
                    break
                xn,yn = move(x,y,i)
                if (xn,yn) not in dead and (xn,yn) not in backsteps:
                    second = i
                    dir = second
                    break
            # print("input ", x,y,second, len(backsteps), i)
            put_result(dict.get(position+1,0), param1, base, int(second))
            position += 2
            
        elif( opcode == 4):
            print_map()
            # print(x,y, first, dir) 
            if first == 0:  
                xw,yw = move(x,y,dir)
                dead.append( (xw,yw) )
                map[ (xw,yw) ] = "#"
            elif first == 1:
                xn, yn = move(x,y,dir)
                if direction == "forward" and (x,y) not in backsteps:
                    backsteps.append( (x,y) )                
                else:
                    direction = "forward"
                x,y = xn,yn
                map[ (x,y) ] = "."
                
            elif first == 2:
                x,y = move(x,y,dir)
                map[ (x,y) ] = "X"
                print_map()
                print("found")
                backtrace(x,y)
                return
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
    print_map()

file = open(sys.argv[1],'r')

file = list(map( int, file.readline().split(",")))
numbers = file.copy()

dict = {}
map = {}

for i in range(len(numbers)):
    dict[i] = numbers[i]

calculate()

