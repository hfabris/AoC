import sys

def get(numbers, possition, node):
	nodes.append(node)
	num_children = int(numbers[possition])
	num_entry = int(numbers[possition+1])
	possition += 2
	for i in range(num_children):
		possition = get(numbers, possition, len(nodes))
	for i in range(num_entry):
		entry[node] = entry.get(node, 0) + int(numbers[possition])
		values[node] = values.get(node,0) + int(numbers[possition])
		possition += 1
	if num_children == 0:
		return possition
	else:
		pos = possition - num_entry
		sum = 0
		for i in range(num_entry):
			if int(numbers[pos+i]) > num_children or int(numbers[pos+i]) == 0:
				sum += 0
			else:
				sum += values[int(numbers[pos+i]) + node]
		values[node] = sum
		return possition
		

file = open(sys.argv[1],'r')
text = file.readline()
file.close()

numbers = text.split(" ")

entry = {}
values = {}
possition = 0
nodes = []

possition = get(numbers, possition, len(nodes))
	
sum = 0
for value in entry.values():
	sum += value
	
print sum
print values[0]
	
	
	
	
	
	
	






















