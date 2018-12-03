import sys
input = open(sys.argv[1],'r')

list = []
frequency = 0
set = [0]

for line in input:
	frequency += int(line)
	list.append(int(line))
	if int(frequency) in set:
		print frequency
	else:
		set.append(int(frequency))

print "Resulting frequency is:", frequency

count = 0		
while(1):
	frequency += list[count]
	if int(frequency) in set:
		break
	else:
		set.append(int(frequency))
	count = (count+1) % len(list)

print "The first frequency my device reaches twice is:", frequency
	


















