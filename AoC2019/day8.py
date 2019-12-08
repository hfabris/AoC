import sys

def get_pixel(i):
    for j in layers:
        if j[i] != "2": return j[i]
    return "2"

file = open(sys.argv[1],'r').readline()

wide = 25
tall = 6

layers = []
numbers = []

for i in range(int(len(file) / (wide * tall))):
    
    zeros = 0
    ones = 0
    twos = 0
    layer = ""
    for j in range(wide * tall):
        layer += file[j + wide*tall*i]
        j = int( file[j + wide*tall*i])
        if j == 0: zeros += 1
        elif j == 1: ones += 1
        elif j == 2: twos += 1
    numbers.append( (zeros,ones,twos))
    layers.append(layer)

numbers.sort( key= lambda x: x[0])
picture = ""


for i in range(len(layers[0])):

    if i % 25 == 0 and i != 0:
        picture += "\n"
    pixel = get_pixel(i) 
    if pixel != "1": picture += " "
    else: picture += pixel
        

print( numbers[0][1] * numbers[0][2])
print(picture)




