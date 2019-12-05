import sys

def turn(turn_option):
	if turn_option == 0:
		return "l"
	elif turn_option == 1:
		return "s"
	else:
		return "r"



file = open(sys.argv[1],'r')

input = file.readlines()
file.close()

oneLeft = False
carts = []
last_pos = []
line_pos = 0
map = []

for line in input:
	sign_pos = 0
	map.append(list(line))
	for sign in line:
		if sign is "<" or sign is ">" or sign is "v" or sign is "^" :
			carts.append((line_pos, sign_pos, sign, 0))
			last_pos.append((sign_pos,line_pos))
			if sign is "<" or sign is ">":
				map[line_pos][sign_pos] = "-"
			else:
				map[line_pos][sign_pos] = "|"
		sign_pos += 1
	
	line_pos += 1

carts.sort()


while not oneLeft:
	crashed = set()
	for i in range(len(carts)):
		
		y_cord,x_cord,dirrection,turn_option = carts[i]
		
		
		if (y_cord,x_cord) in crashed:
			continue
		
		if dirrection is "<":				
			x_cord -= 1
			last_sign = map[y_cord][x_cord]
			if last_sign is "/":
				dirrection = "v"
			elif last_sign is "+":
				turn_dirrection = turn(turn_option)
				if turn_dirrection is "l":
					dirrection = "v"
				elif turn_dirrection is "r":
					dirrection = "^"
				turn_option = (turn_option+1) % 3
			elif last_sign is not "-" and last_sign is not "|":
				dirrection = "^"
		
		elif dirrection is ">":
			x_cord += 1
			last_sign = map[y_cord][x_cord]
			if last_sign is "/":
				dirrection = "^"
			elif last_sign is "+":
				turn_dirrection = turn(turn_option)
				if turn_dirrection is "l":
					dirrection = "^"
				elif turn_dirrection is "r":
					dirrection = "v"
				turn_option = (turn_option+1) % 3
			elif last_sign is not "-" and last_sign is not "|":
				dirrection = "v"
		
		elif dirrection is "^":
			y_cord -= 1
			last_sign = map[y_cord][x_cord]
			if last_sign is "/":
				dirrection = ">"
			elif last_sign is "+":
				turn_dirrection = turn(turn_option)
				if turn_dirrection is "l":
					dirrection = "<"
				elif turn_dirrection is "r":
					dirrection = ">"
				turn_option = (turn_option+1) % 3
			elif last_sign is not "-" and last_sign is not "|":
				dirrection = "<"
		
		else:
			y_cord += 1
			last_sign = map[y_cord][x_cord]
			if last_sign is "/":
				dirrection = "<"
			elif last_sign is "+":
				turn_dirrection = turn(turn_option)
				if turn_dirrection is "l":
					dirrection = ">"
				elif turn_dirrection is "r":
					dirrection = "<"
				turn_option = (turn_option+1) % 3
			elif last_sign is not "-" and last_sign is not "|":
				dirrection = ">"
					
		for sec_cart in carts:
			y,x,d,t = sec_cart
			if x_cord == x and y_cord == y:
				crashed.add((y_cord,x_cord))					
				print "Crash: x = ",x_cord, "y = ",y_cord
			
		carts[i] = (y_cord,x_cord,dirrection, turn_option)		
		
	
	carts = [c for c in carts if (c[0], c[1]) not in crashed]
	carts.sort()
	if len(carts) == 1:
		print carts
		break