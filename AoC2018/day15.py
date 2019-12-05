import sys

def get_dist(x2,x1, y2,y1):
	return abs(x2-x1) + abs(y2-y1)

def get_name(x,y, type):
	if type is "E":
		for elf in elfs_pos:
			xe,ye, hpe = elfs_pos[elf]
			if xe == x and ye == y:
				return elf
	else:
		for goblin in goblins_pos:
			xg,yg, hpg = goblins_pos[goblin]
			if xg == x and yg == y:
				return goblin

def delete(name):
	if name.startswith("E"):
		del elfs_pos[name]
	else:
		del goblins_pos[name]
	for i in characters:
		if name == i:
			del characters[name]
			break
	
	
		
def bfs(x,y,name):
	path = ((x,y),)
	L = [path]
	Visited = []
	while L != []:
		path = L.pop(0)
		x1,y1 = path[-1]
		Visited.append((x1,y1))
		if map[y1-1][x1] is "G" and name is "E" or map[y1-1][x1] is "E" and name is "G": return path + ((x1,y1-1),)
		elif (x1,y1-1) not in Visited and map[y1-1][x1] is ".": L.append(path+((x1,y1-1),)) 
		
		if map[y1][x1-1] is "G" and name is "E" or map[y1][x1-1] is "E" and name is "G": return path + ((x1-1,y1),)
		elif (x1-1,y1) not in Visited and map[y1][x1-1] is ".": L.append(path+((x1-1,y1),)) 
		
		if map[y1][x1+1] is "G" and name is "E" or map[y1][x1+1] is "E" and name is "G": return path + ((x1+1,y1),)
		elif (x1+1,y1) not in Visited and map[y1][x1+1] is ".": L.append(path+((x1+1,y1),)) 

		if map[y1+1][x1] is "G" and name is "E" or map[y1+1][x1] is "E" and name is "G": return path + ((x1,y1+1),)
		elif (x1,y1+1) not in Visited and map[y1+1][x1] is ".": L.append(path+((x1,y1+1),))
	

def f(elem):
	y,x,hp = characters[elem]
	return y,x
	
file = open(sys.argv[1],'r')
input = file.readlines()
file.close()

characters = {}
elfs = 0
elfs_pos = {}
goblins = 0
goblins_pos = {}
y = 0
map = []

for line in input:
	map.append(list(line))
	for x in range(len(line)):
		if line[x] is "E":
			elfs += 1
			characters["E"+str(elfs)] = (y,x,200)
			elfs_pos["E"+str(elfs)] = (x,y, 200)
		elif line[x] is "G":
			goblins += 1
			characters["G"+str(goblins)] = (y,x, 200)
			goblins_pos["G"+str(goblins)] = (x,y, 200)
	y += 1


done = False
round = 1
	
while not done:
	sorted_char =  sorted(characters.items(), key=lambda x: x[1])
	dead = set()
	allAlive = True
	for character in sorted_char:
		y,x,hp = character[1]
		name = character[0]
		closest = 200
		best = ()
		if name.startswith("E"):	
			x,y,hp = elfs_pos[name]
			if hp > 0:
				best = bfs(x,y,"E")
				if best != None:
					xg, yg = best[1]
					if map[yg][xg] is ".":
						map[yg][xg] = "E"
						map[y][x] = "."
						elfs_pos[name] = (xg,yg,hp)
						characters[name]= (yg,xg,hp)
						x = xg
						y = yg
			
				attack = ()
				hp_min = 201
				if map[y-1][x] is "G" and goblins_pos[get_name(x,y-1,"G")][2] < hp_min:
					attack = (x,y-1)
					hp_min = goblins_pos[get_name(x,y-1,"G")][2]
				if map[y][x-1] is "G" and goblins_pos[get_name(x-1,y,"G")][2] < hp_min:
					attack = (x-1,y)
					hp_min = goblins_pos[get_name(x-1,y,"G")][2]
				if map[y][x+1] is "G" and goblins_pos[get_name(x+1,y,"G")][2] < hp_min:
					attack = (x+1,y)
					hp_min = goblins_pos[get_name(x+1,y,"G")][2]
				if map[y+1][x] is "G" and goblins_pos[get_name(x,y+1,"G")][2] < hp_min:
					attack = (x,y+1)
					hp_min = goblins_pos[get_name(x,y+1,"G")][2]
			
				if len(attack) > 0:
					nameg = get_name(attack[0],attack[1], "G")
					xg,yg, hpg = goblins_pos[nameg]
					hpg -= 3
					if hpg < 0:
						map[attack[1]][attack[0]] = "."
						dead.add(nameg)
					goblins_pos[nameg] = (xg,yg,hpg)
					characters[nameg]= (yg,xg, hpg)
			else:
				allAlive = False
			
		else:
			
			x,y,hp = goblins_pos[name]
			if hp > 0:
				best = bfs(x,y,"G")
				if best != None:
					xe, ye = best[1]
					if map[ye][xe] is ".":
						map[ye][xe] = "G"
						map[y][x] = "."
						goblins_pos[name] = (xe,ye,hp)
						characters[name]= (ye,xe,hp)
						y = ye
						x = xe
				
				attack = ()
				hp_min = 201
				if map[y-1][x] is "E" and elfs_pos[get_name(x,y-1,"E")][2] < hp_min and elfs_pos[get_name(x,y-1,"E")][2] > 0:
					attack = (x,y-1)
					hp_min = elfs_pos[get_name(x,y-1,"E")][2]
				if map[y][x-1] is "E" and elfs_pos[get_name(x-1,y,"E")][2] < hp_min and elfs_pos[get_name(x-1,y,"E")][2] > 0:
					attack = (x-1,y)
					hp_min = elfs_pos[get_name(x-1,y,"E")][2]
				if map[y][x+1] is "E" and elfs_pos[get_name(x+1,y,"E")][2] < hp_min and elfs_pos[get_name(x+1,y,"E")][2] > 0:
					attack = (x+1,y)
					hp_min = elfs_pos[get_name(x+1,y,"E")][2] 
				if map[y+1][x] is "E" and elfs_pos[get_name(x,y+1,"E")][2] < hp_min and elfs_pos[get_name(x,y+1,"E")][2] > 0:
					attack = (x,y+1)
					hp_min = elfs_pos[get_name(x,y+1,"E")][2]
				if len(attack) > 0:
				
					namee = get_name(attack[0],attack[1], "E")
					xe,ye, hpe = elfs_pos[namee]
					hpe -= 3
					if hpe < 0:
						map[attack[1]][attack[0]] = "."
						dead.add(namee)
					elfs_pos[namee] = (xe,ye,hpe)
					characters[namee] = (ye,xe,hpe)
			else:
				allAlive = False
	
	
	if len(dead) > 0:
		for name in dead:
			delete(name)
	
			
	if len(elfs_pos) == 0 or len(goblins_pos) == 0 or round > 60:
		done = True
	if allAlive:
		round += 1
	
print round			
for i in range(len(map)):
	print "".join(map[i])
	
healt = 0
if len(goblins_pos) == 0:
	for elf in elfs_pos:
		xe,ye,hpe = elfs_pos[elf]
		print xe,ye,hpe, elf
		healt += hpe
else:
	for goblin in goblins_pos:
		xg,yg,hpg = goblins_pos[goblin]
		print xg,yg,hpg
		healt += hpg

print healt * (round)


















