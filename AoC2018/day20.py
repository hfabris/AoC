def recursion(pos, distance,count):
	dist = []
	lenght = 0
	while line[pos] not in [")","$"]:
		if line[pos] in ["E","W","S", "N"]:
			lenght += 1
		
		if (line[pos] is "E" and line[pos-1] is "W") or (line[pos] is "W" and line[pos-1] is "E") or (line[pos] is "S" and line[pos-1] is "N") or (line[pos] is "N" and line[pos-1] is "S"):
			if distance+lenght > 1000:
				count += 1
			lenght = -9999
		if line[pos] is "|":
			if lenght < 0: lenght = 0
			elif distance+lenght > 1000:
				count += 1
			dist.append(lenght)
			lenght = 0
		
		if line[pos] is "(":
			pos, move,count = recursion(pos+1, distance+lenght,count)
			lenght += move
		pos += 1
	dist.append(lenght)
	return [pos,max(dist),count]
	

file = open("day20.txt","r")
line = file.readline()
file.close()


pos = 0
doors = 0
lenght = len(line)
count = 0
while pos < lenght:
	if line[pos] in ["E","W","S", "N"]:
		doors += 1
	elif line[pos] is "(":
		pos, move,count = recursion(pos+1, doors, count)
		pos-= 1
		doors += move
	pos += 1
print doors+1, count

















