import sys, math

def check_materials(product, to_produce):
    quantity, materials = reactions[product]
    for material in materials.split(", "):
        needed, name = material.split(" ")
        if extra.get(name,0) < (int(needed) * to_produce): return False 
    return True
        
def reaction(material, how_much):
    if check_materials(material,how_much):
        quantity, resources = reactions[material]
        for resource in resources.split(", "):
            needed, name = resource.split(" ")
            extra[name] -= (int(needed)*how_much)
        extra[material] = extra.get(material,0) + (reactions[material][0]*how_much)        

def produce(material, quantity, ore):
    repeats = int( math.ceil( quantity / reactions[material][0] ) )
    while not check_materials(material, repeats):
        for resource in reactions[material][1].split(", "):
            
            needed, name = resource.split(" ")
            needed = int(needed) 
            have = int(extra.get(name,0))
            if have < needed * repeats: 
                diff = needed * repeats - have
                if name == "ORE":
                    ore += repeats * needed
                    extra[name] = extra.get(name,0) + repeats * needed
                else:
                    ore = produce(name, diff, ore)
    reaction(material, repeats)
    return ore

def empty():
    for key in extra.keys():
        extra[key] = 0

def search(high, low, amount):
    while high - low > 1:
        empty()
        val = low + ( high - low ) // 2
        t = produce("FUEL", val,0)
        if t > amount:
            high = val
        else:
            low = val
    return low

file = open(sys.argv[1], "r")

reactions = {}
extra = {}

for line in file:
    materials, product = line.split("=>")
    quantity, name = product.strip().split(" ")
    reactions[name] = (int(quantity),materials.strip())
     
stock = 1000000000000

print( produce("FUEL", 1, 0) )
empty()
produced = search(stock, 0, stock)

print( produced )
    
    