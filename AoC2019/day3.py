import sys

def calc_direction(x,y, direction):
    if direction == "R":
        x += 1
    elif direction == "L":
        x -= 1
    elif direction == "U":
        y += 1
    elif direction == "D":
        y -= 1
    return x,y

input = open(sys.argv[1],'r')

lines = input.readlines()

map = {}

x,y = 0,0

for path in lines[0].split(","):
    direction = path[0]
    distance = int(path[1:])
    for i in range(distance):
        x,y = calc_direction(x,y,direction)
        map[(x,y)] = "."

intersections = []

x,y = 0,0

for path in lines[1].split(","):
    direction = path[0]
    distance = int(path[1:])
    for i in range(distance ):
        x,y = calc_direction(x,y,direction)
        if( map.get( (x,y), "0") == "."):
            intersections.append( (x,y) )

            
print(intersections,  min( [abs(x) + abs(y) for x,y in intersections]))

steps = 0
step = {}
x,y = 0,0

for path in lines[0].split(","):
    direction = path[0]
    distance = int(path[1:])
    for i in range(distance):
        x,y = calc_direction(x,y,direction)
        steps += 1
        if( (x,y) in intersections):
            step[(x,y)] = steps

x,y = 0,0
steps = 0

for path in lines[1].split(","):
    direction = path[0]
    distance = int(path[1:])
    for i in range(distance ):
        x,y = calc_direction(x,y,direction)
        steps += 1
        if( (x,y) in intersections):
            step[(x,y)] = step[(x,y)] + steps
 

print( min(step.values())) 
            
            
            
            
            
            
            