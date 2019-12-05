def Manhattan(x1,y1,z1,x,y,z):
	return abs(x1-x)+abs(y1-y)+abs(z1-z)

file = open("day23.txt", "r")
lines = file.readlines()
file.close()


max_radius = 0
x,y,z = 0,0,0

for line in lines:
	radius = int(line.split("=")[2].strip())
	if radius > max_radius:
		cord = line.split("<")[1].split(">")[0].split(",")
		x,y,z = [int(x) for x in cord]
		max_radius = radius

print max_radius		
in_range = 0
		
for line in lines:		
	x1,y1,z1 = [int(k) for k in line.split("<")[1].split(">")[0].split(",")]
	d = Manhattan(x1,y1,z1, x,y,z)
	# print d, max_radius
	if d <= max_radius:
		in_range += 1
		
# print max_radius,x,y,z
print in_range



















