import sys, math

def look(x,y, x0, y0, map):
    if x < 0 or y < 0 or x >= width or y >= height: return 0
    if map[x+y*width] == "#":
        i = 2
        dx = x - x0
        dy = y - y0
        if dx == 0: dy //= abs(dy)
        elif dy == 0: dx //= abs(dx)
        elif math.gcd(dx, dy) != 1:
            gcd = math.gcd(dx, dy)
            dx //= gcd
            dy //= gcd
        while True:
            if x0+i*dx < 0 or y0+i*dy < 0 or x0+i*dx >= width or y0+i*dy >= height: break
            map[x0+i*dx+(y0+i*dy)*width] = "."
            i += 1
        map[x+y*width] = "."
        return 1
    return 0

    
def search(x,y, map):
    around = []
    
    
    for i in range(1,max(width +1, height +1)):
        for j in range(-1*i, i+1):
            
            if look(x+j, y-i, x,y,map):
                around.append((x+j, y-i))
            if look(x-i, y+j, x,y,map):
                around.append((x-i, y+j))
            if look(x-j, y+i, x,y,map):
                around.append((x-j, y+i))
            if look(x+i, y-j, x,y,map):
                around.append((x+i, y-j))
    
    return around    

def part2(x,y,map):
    
    seen = search(x,y,list(map))
    quadrant = {}
    quadrant[1] = []
    quadrant[2] = []
    quadrant[3] = []
    quadrant[4] = []
     
    for xa, ya in seen:
        if xa < x:
            if ya > y:
                quadrant[3].append((xa,ya))
            else:
                quadrant[2].append((xa,ya))
        else:
            if ya > y:
                quadrant[4].append((xa,ya))
            else:
                quadrant[1].append((xa,ya))
     
    current = len(quadrant[1]) + len(quadrant[4]) + len(quadrant[3])
    
    q3 = []
    
    for xa,ya in quadrant[2]:
        
        c = math.sqrt((xa-x)**2 + (ya-y)**2)
        angle = math.cos( (ya-y) / c )
        q3.append( (angle,xa, ya) )
            
    q3.sort(key = lambda x : -1 * x[0])
    
    c200, x200, y200 = q3[200-current-1]
    print("200th destroyed asteroid is at possition: ", x200, y200)
    print( x200 * 100 + y200)
    
    

file = open(sys.argv[1],'r')

x,y = 0,0
width, height = 0,0
asteroids = []
map = ""

for line in file:
    x = len(line)
    map += line.strip()
    for i in range(x):
        if line[i] == "#":
            asteroids.append((i,y))
    y += 1
    width, height = x,y

maximum = 0
xb, yb = 0,0

for x,y in asteroids:
    
    detected = len(search(x,y,list(map)))
    if detected > maximum:  
        maximum = detected
        xb, yb = x,y
    
print("Maximum number of detected asteroids: ", maximum, ", coordinates of best location: ", xb,yb)


part2(xb,yb, map)
    