import sys,numpy

file = open(sys.argv[1],'r')
text = file.readlines()
file.close()

letters = []
order = {}
deppendency = {}
ready = set()
deppend = set()
correct = ""

for line in text:
	step_start = line.split(" ")[1]
	step_end = line.split(" ")[7]
	letters.append(step_start)
	order[step_start] = order.get(step_start, "") + step_end
	deppendency[step_end] = deppendency.get(step_end, "") + step_start
	deppend.add(step_end)
	ready.add(step_start)

for letter in deppend:
	if letter in ready:
		ready.remove(letter)
		
workers = numpy.zeros(5)
works = {}
second = 0


while len(ready) > 0 or len(deppend) > 0 or workers.any() != 0:
	worker = 0
	for i in range(len(workers)):
		if workers[i] == 0:
			worker = i + 1
			if len(ready) > 0:
				next = list(ready)[0]
			else:
				next = "a"
			for letter in ready:
				if ord(letter) < ord(next):
					next = letter
			if next != "a":
				workers[worker-1] = str(ord(next)-65+1 + 60)
				works[worker-1] = next
				ready.remove(next)		
	second += 1
	for i in range(len(workers)):
		if workers[i] > 0:
			workers[i] = workers[i] - 1
			if workers[i] == 0:
				work = works.get(i,"")
				if work != "":
					next = work
					correct += next
					works[i] = ""
	
					for letter in order.get(next,""):
						deppendency[letter] = deppendency[letter].replace(next, "")
						if len(deppendency[letter]) == 0:
							ready.add(letter)
							deppend.remove(letter)
	
print correct, 	second
















