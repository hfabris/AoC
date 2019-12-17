import sys, numpy, math

file = open(sys.argv[1], "r").readline()

pattern = ["0","1","0","-1"]


for step in range(100):
    next = numpy.zeros(len(file), dtype = int)
    
    for pos in range(len(file)):
        t = [0,1,0,-1]
        t = [pattern[math.floor( x / (pos+1))] for x in range(len(t)*(pos+1))]
        for i in range(len(file)):
            next[pos] += int(t[(i+1)%len(t)]) * int(file[i])
        
    file = ""
    for n in next:
        if n < 0: n *= -1
        file += str(n%10)
        
print( file[:8] )
        
        
        
        
        
        
        
    
    


