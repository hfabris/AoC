import sys, math

def calc_fuel(mass):
    return math.floor( num / 3) - 2


input = open(sys.argv[1],'r')

sum = 0


for line in input:
    num = int(line)
    
    while( True ):
        num = calc_fuel(num)
        if( num <= 0): break
        #print( num )
        sum += num
    
print(sum)
