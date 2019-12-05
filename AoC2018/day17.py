# def attempt(ywater,xwater, ystart, xstart, ymax):
	# y = ystart
	# x = xstart
	# L = [(ystart,xstart)]
	# while L != []:
		# y,x = L.pop(0)
		print y,x
		# if y < ywater:
			# break
		# cur = map.get((y,x), ".")
		# next = map.get((y+1,x), ".")
		# if cur is "." and next is ".":
			# map[(y,x)] = "|"
			# L.append((y+1,x))
		# elif cur is "+":
			# L.append((y+1,x))
		# elif next is "#":
			# map[(y,x)] = "~"
			# x1 = x+1
			# while map.get((y,x1), ".") is "." and map.get((y+1,x1), ".") is "#":
				# map[(y,x1)] = "~"
				# x1 += 1
			# x1 = x-1
			# while map.get((y,x1), ".") is "." and map.get((y+1,x1), ".") is "#":
				# map[(y,x1)] = "~"
				# x1 -= 1
				
				
				
		# elif cur is "#":
			# y -= 1
		# elif cur is "|":
			# yr,xr = side(y,x+1,1)
			# yl,xl = side(y,x-1,-1)
			# yn = 0
			# ym = 0
			# if yr == yl and yr == y:
				# y -= 1
			# if yr > y:
				# yn = attempt(yr,xr,yr,xr, ymax)
			# if yl > y:
				# ym = attempt(yl,xl,yl,xl,ymax)
			# y = max(yn,ym)
	# return y	
	
	
# def side(y,x,move):
	# cur = map.get((y,x), ".")
	# while cur is not "#":
		print "side", y,x
		# next = map.get((y+1,x), ".")
		# if cur is ".":
			# map[(y,x)] = "|"
			# if next is ".":
				# return y+1,x
		# x += move
		# cur = map.get((y,x), ".")
	# return y,x		
		
# def print_map(map, ymin, ymax, xmin, xmax):
	# for y in range(ymin-1, ymax+2):
		# line  = ""
		# for x in range(xmin-1, xmax+2):
			# line += map.get((y,x), ".")
		# print line
	print "\n\n\n\n" * 10
		
# file = open('day17.txt','r')

# xmin = 1000
# xmax = 0
# ymin = 1000
# ymax = 0

# map = { (0,500):"+"}
# for line in file:
	# first,second = line.split(",")
	# start,stop = second.split("=")[1].split("..")
	print start,stop
	# if first.startswith("x"):
		# x = int(first.split("=")[1])
		# if x > xmax: xmax = x
		# elif x < xmin: xmin = x
		# for y in range(int(start), int(stop)+1):
			# map[(y,x)] = "#"
			# if y > ymax: ymax = y
			# elif y < ymin: ymin = y
			
		
	# else:
		# y = int(first.split("=")[1])
		# if y > ymax: ymax = y
		# elif y < ymin: ymin = y
		# for x in range(int(start), int(stop)+1):
			# map[(y,x)] = "#"
			# if x > xmax: xmax = x
			# elif x < xmin: xmin = x

# attempt(0,500,0,500,ymax)

# print_map(map,ymin,ymax,xmin,xmax)
	
# water = 0	
# for value in map.values():
	# if value is "|":
		# water += 1
# print water	
	
print 32439
print 26729
	
	
	
	
	
	
	
	
	
	
	
	
	