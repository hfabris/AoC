import sys

def diff(string1, string2):
	dif = 0
	for x,y in zip(string1, string2):
		if x != y:
			dif += 1
	return dif

def sub(string1, string2):
	line = ""
	for i in range(len(string1)-1):
		if(string1[i] == string2[i]):
			line += string1[i]
	return line


input = open(sys.argv[1],'r')

double = 0
triple = 0
text = []

for line in input:
	dict = {}
	text.append(line)
	for letter in line:
		dict[letter] = dict.get(letter,0) + 1
	if 2 in dict.values():
		double += 1
	if 3 in dict.values():
		triple += 1
print "Checksum is", double*triple
		
for i in range(len(text)):
	for j in range(i,len(text)):
		if diff(text[i], text[j]) == 1:
			print "Common letters between the two correct box IDs:", sub(text[i], text[j])
		
		
		

