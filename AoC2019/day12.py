import sys, numpy, itertools, math,copy

def lcm(num1, num2):
    return (num1 * num2) // math.gcd(num1,num2)

def repeat(step, coord):
    for i in range(4):
        if moons[i][coord] != initial[i][coord]: return -1
    return step


file = open(sys.argv[1],'r')

moons = []
velocity = numpy.zeros((4,3))

for line in file:
    line = line.strip()[1:-1].split(",")
    position = []
    for x in line:
        y = int(x.split("=")[1])
        position.append(y)
    moons.append(position)

initial = copy.deepcopy(moons)

sum = 0
steps = 0
repeats = numpy.zeros(3)

while True:
    for j in itertools.combinations(range(4), r = 2):
        vel1 = velocity[j[0]]
        vel2 = velocity[j[1]]
        for z in range(3):
            if moons[j[0]][z] < moons[j[1]][z]:
                vel1[z] += 1
                vel2[z] -= 1
            elif moons[j[0]][z] > moons[j[1]][z]:
                vel1[z] -= 1
                vel2[z] += 1
        velocity[j[0]] = vel1
        velocity[j[1]] = vel2
    
    sum = 0
    
    for j in range(4):
        pos = moons[j]
        vel = velocity[j]
        potential = 0
        kinetic = 0
        for z in range(3):
            pos[z] += vel[z]
            potential += abs(moons[j][z])
            kinetic += abs(velocity[j][z])
        sum += potential * kinetic    
    
    steps += 1
    
    if( steps == 1000): print(sum)
    
    for j in range(3):
        if repeat(steps, j) > 0 and repeats[j] == 0:
            repeats[j] = repeat(steps,j)+1
            
    if numpy.all(repeats != numpy.zeros(3)): 
        print(lcm(int(repeats[0]), lcm(int(repeats[1]), int(repeats[2]))))   
        break
    