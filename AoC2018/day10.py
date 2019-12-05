import sys

file = open(sys.argv[1],'r')
text = file.readlines()
file.close()

pairs = {}

for line in text:
	position = line.split("v")[0]
	velocity = line.split("v")[1]
	
	position = position[10:-2]
	positionX, positionY = position.split(",")
	
	velocity = velocity[9:-2]
	velocityX, velocityY = velocity.split(",")
	
	
	pairs[(int(positionX), int(positionY))] = (int(positionX), int(positionY), int(velocityX), int(velocityY))




for seconds in range(1,20000):
	
	cur_minX = 30562
	cur_minY = 30562
	cur_maxX = -30562
	cur_maxY = -30562
	
	current_pairs = []
	for pair in pairs.keys():
		positionX, positionY, velocityX, velocityY = pairs[pair]
		
		positionX += velocityX
		positionY += velocityY
		
		if positionX > cur_maxX:
			cur_maxX = positionX
		elif positionX < cur_minX:
			cur_minX = positionX
		if positionY > cur_maxY:
			cur_maxY = positionY
		elif positionY < cur_minY:
			cur_minY = positionY
		
		pairs[pair] = (positionX,positionY,velocityX, velocityY)
		current_pairs.append( (positionX,positionY) )
	if cur_maxX - cur_minX < 100 and cur_maxY - cur_minY < 100:
		result = []
		for j in range(cur_minY, cur_maxY+1):
			for i in range(cur_minX, cur_maxX+1):
				if (i,j) in current_pairs:
					result.append("#")
				else:
					result.append(".")
			result.append("\n")
		print seconds	
		print "".join(result)
		print "\n"
		
			


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	