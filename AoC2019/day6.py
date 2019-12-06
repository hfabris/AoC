import sys, time

def add_list(system, list, steps, visited):
    for object in orbits.get(system, "")[:-1].split(","):
        if object not in visited and object != "":
            list.append( (object, steps) )
    return list

def search(system, end, steps):
    visited = []
    to_search = add_list(system,  [], steps, visited)
    while to_search:
        n,x = to_search.pop()
        visited.append(n)
        if n == end: 
            return x
        to_search = add_list(n,  to_search, x+1, visited)
        to_search = sorted(to_search, key = lambda x: x[1])
    return -1
       

def get_transfers(start, end):
    system = in_orbit[start][:-1]
    steps = 0
    calculated = -1
    while calculated < 0:
        calculated = search(system, end,  steps)        
        system = in_orbit[system][:-1]
        steps += 1
    return calculated

def calculate(node, depth):
    sum = 0
    if orbits.get(node, "") == "" : return depth
    for child in orbits[node][:-1].split(","):
        sum += calculate(child,  depth + 1)
    return sum + depth
      

    
file = open(sys.argv[1],'r').readlines()

in_orbit = {}
orbits = {}

root = "COM"

for line in file:
    object1, object2 = line.strip().split(")")
    in_orbit[object2] = in_orbit.get(object2, "") + object1 + "," 
    orbits[object1] = orbits.get(object1, "") + object2 + "," 
     
        
print(calculate(root, 0))
    
start = "YOU"
end = "SAN"

print( get_transfers(start, end))



    