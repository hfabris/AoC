import sys

input = open(sys.argv[1],'r')

dict = {}
overlap = 0
size = {}

for line in input:
	x0,y0 = line.split(" ")[2].split(",")
	y0 = y0[:-1]
	
	x,y = line.split(" ")[3].strip().split("x")
	size[line.split(" ")[0]] = int(x) * int(y)
	for X in range(int(x)):
		for Y in range(int(y)):
			dict[ (int(x0)+1+X, int(y0)+1+Y) ] = dict.get((int(x0)+1+X, int(y0)+1+Y), "") + line.split(" ")[0]
		
			
for value in dict.values():
	if value.count("#") > 1:
		overlap += 1
	else:
		size[value] -= 1
		if(size[value] == 0):
			print value, "does not overlap with anyone"

print overlap, "square inches of fabric are within two or more claims?"

	

	
	
	
	
	



















