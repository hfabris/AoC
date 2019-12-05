import sys

file = open(sys.argv[1],'r')
text = file.readlines()
file.close()

grid = {}
count = 0
maxX = 0
maxY = 0

for line in text:
	x,y = line.strip().split(",")
	grid["A"+str(count)] = (int(x),int(y))
	if int(x) > maxX:
		maxX = int(x)
	if int(y) > maxY:
		maxY = int(y)
	count += 1
	
rub = []
count = {}
max_distance = 10000	
num_less = 0
for i in range(maxX):
	for j in range(maxY):
		dist = {}
		for key in grid.keys():
			current_distance = abs(i - grid[key][0]) + abs(j - grid[key][1])
			dist[(key,i,j)] = current_distance
		if sum(dist.values()) < 10000:
			num_less += 1
		closest = min(dist.values())
		close = ""
		for dis in dist.keys():
			if dist[dis] == closest:
				close += dis[0]
		if len(close) == 2 or len(close) == 3:
			count[close] = count.get(close,0) + 1
			if j == 0 or i == 0:
				rub.append(close)
		
print num_less	
	
max = 0
for key in count.keys():
	if key not in rub:
		if count[key] > max:
			max = count[key]
			
		
print max			
			
















