def get_adjacent(x,y):
	ground = 0
	trees = 0
	lumberyard = 0
	dir = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
	for dx,dy in dir:
		if x+dx >= xmin and x+dx <= xmax and y+dy >= ymin and y+dy <= ymax:
			# print x+dx, y+dy, x,y
			cur = field[y+dy][x+dx]
			if cur is ".": ground += 1
			elif cur is "|": trees += 1
			else: lumberyard += 1
	return [ground,trees,lumberyard]
	

file = open("day18.txt","r")

field = []
xmax = 49
xmin = 0
ymin = 0
ymax = 49




for line in file:
	field.append(line.strip())
	
polje = []	
	
for i in range(1000):
	new_field = []
	trees_count = 0
	lumberyard_count = 0
	for y in range(ymax+1):
		line = ""
		for x in range(xmax+1):
			# print line
			ground,trees,lumberyard = get_adjacent(x,y)
			cur = field[y][x]
			# print cur,ground,trees,lumberyard
			if cur is ".":
				if trees >= 3:
					line += "|"
					trees_count += 1
				else:
					line += "."
			elif cur is "|" :
				if lumberyard >= 3:
					line += "#"
					lumberyard_count += 1
				else:
					line += "|"
					trees_count += 1
			elif cur is "#":
				if lumberyard >= 1 and trees >= 1:
					line += "#"
					lumberyard_count += 1
				else:
					line += "."
		new_field.append(line)
	field = new_field
	# print trees_count, lumberyard_count, trees_count * lumberyard_count
	polje.append((trees_count,lumberyard_count))
	
for i in range(len(field)):
	print field[i]

print trees_count * lumberyard_count		

minutes = (1000000000 - 846) % 28

print polje[845+14], polje[845+minutes][0] * polje[845+minutes][1] 





















