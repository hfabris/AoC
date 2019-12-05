import sys

file = open(sys.argv[1],'r')

input = file.readline().split(" ")[2].strip()
file.readline()

rules = {}

for line in file.readlines():
	rules[line.split("=>")[0].strip()] = line.split("=>")[1].strip()

	
input = str(input)
start = 0
sum_last = 0

for i in range(500):
	input = "...." + input + "...."
	start -= 3
	next_get = ""
	for j in range(2,len(input)-2):
		check = input[j-3:j+2]
		if check in rules:
			next_get += rules[check]
		else:
			next_get += "."
	input = next_get
	sum_cur = 0	
	for k in range(len(input)):
		if input[k] == "#":
			sum_cur += k + start
	diff = sum_cur - sum_last
	sum_last = sum_cur
	if i == 19: print sum_cur

	
left = (50000000000 - i-1) * 45 + sum_cur
print left
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	