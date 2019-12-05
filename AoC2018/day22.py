
depth = 11991
targetx, targety = 6,797

risk = 0
map = {}
list = []

for y in range(targety+1):
	for x in range(targetx+1):
		
		
		geological = 0
		if x == targetx and y == targety:
			geological = 0
		elif y == 0:
			geological = x * 16807
			# map[(x,y)] = geological
			list.append(geological)
		elif x == 0:
			geological = y * 48271
			# map[(x,y)] = geological
			list.append(geological)
		else:
			# geological1 = list[y*targetx + x-1] * list[(y-1) * targetx + x]
			geological = map.get((x-1,y),0) * map.get((x,y-1),0)
			
			# list.append(geological)
		map[(x,y)] = geological % 20183
		erosion = (geological + depth) % 20183
		type = erosion % 3
		risk += type
		
print risk

	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		