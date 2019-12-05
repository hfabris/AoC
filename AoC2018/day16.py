from collections import Counter
def addr(before, order):
	instruction, A, B, C = order
	a = before[A]
	b = before[B]
	before[C] = a + b
	return before

def addi(before, order):
	instruction, A, B, C = order
	a = before[A]
	before[C] = a + B
	return before
	
def mulr(before, order):
	instruction, A, B, C = order
	a = before[A]
	b = before[B]
	before[C] = a * b
	return before

def muli(before, order):
	instruction, A, B, C = order
	a = before[A]
	before[C] = a * B
	return before

def banr(before, order):
	instruction, A, B, C = order
	a = before[A]
	b = before[B]
	before[C] = a & b
	return before	

def bani(before, order):
	instruction, A, B, C = order
	a = before[A]
	before[C] = a & B
	return before		

def borr(before, order):
	instruction, A, B, C = order
	a = before[A]
	b = before[B]
	before[C] = a | b
	return before	

def bori(before, order):
	instruction, A, B, C = order
	a = before[A]
	before[C] = a | B
	return before	

def setr(before, order):
	instruction, A, B, C = order
	a = before[A]
	before[C] = a
	return before
	
def seti(before, order):
	instruction, A, B, C = order
	before[C] = A
	return before	
	
def gtir(before, order):
	instruction, A, B, C = order
	b = before[B]
	if A > b:
		before[C] = 1
	else:
		before[C] = 0
	return before
	
def gtri(before, order):
	instruction, A, B, C = order
	a = before[A]
	if a > B:
		before[C] = 1
	else:
		before[C] = 0
	return before	
	
def gtrr(before, order):
	instruction, A, B, C = order
	a = before[A]
	b = before[B]
	if a > b:
		before[C] = 1
	else:
		before[C] = 0
	return before		
	
def eqir(before, order):
	instruction, A, B, C = order
	b = before[B]
	if A == b:
		before[C] = 1
	else:
		before[C] = 0
	return before
	
def eqri(before, order):
	instruction, A, B, C = order
	a = before[A]
	if a == B:
		before[C] = 1
	else:
		before[C] = 0
	return before	
	
def eqrr(before, order):
	instruction, A, B, C = order
	a = before[A]
	b = before[B]
	if a == b:
		before[C] = 1
	else:
		before[C] = 0
	return before		

	
file = open("day16.txt","r")
lines = file.readlines();
file.close()
 

total = 0
num_line = 0
dict = {}

for i in range(0,len(lines),4):
	
	if lines[i] == "\n":
		break
	num_line += 4
	before = [int(x.strip()) for x in lines[i].split(":")[1][2:-2].split(",")]
	order = [int(x.strip()) for x in lines[i+1].split(" ")]
	after = [int(x.strip()) for x in lines[i+2].split("[")[1][0:-2].split(",")]
	count = 0
	if addr(before[:],order) == after: count += 1; dict["addr"]= dict.get("addr", []) + [order[0]]
	if addi(before[:],order) == after: count += 1; dict["addi"]= dict.get("addi", []) + [order[0]]
	
	if mulr(before[:], order) == after: count += 1; dict["mulr"]= dict.get("mulr", []) + [order[0]]
	if muli(before[:], order) == after: count += 1; dict["muli"]= dict.get("muli", []) + [order[0]]

	if banr(before[:], order) == after: count += 1; dict["banr"]= dict.get("banr", []) + [order[0]]
	if bani(before[:], order) == after: count += 1; dict["bani"]= dict.get("bani", []) + [order[0]]
	
	if borr(before[:], order) == after: count += 1; dict["borr"]= dict.get("borr", []) + [order[0]]
	if bori(before[:], order) == after: count += 1; dict["bori"]= dict.get("bori", []) + [order[0]]
	
	if setr(before[:], order) == after: count += 1; dict["setr"]= dict.get("setr", []) + [order[0]]
	if seti(before[:], order) == after: count += 1; dict["seti"]= dict.get("seti", []) + [order[0]]
	
	if gtir(before[:], order) == after: count += 1; dict["gtir"]= dict.get("gtir", []) + [order[0]]
	if gtri(before[:], order) == after: count += 1; dict["gtri"]= dict.get("gtri", []) + [order[0]]
	if gtrr(before[:], order) == after: count += 1; dict["gtrr"]= dict.get("gtrr", []) + [order[0]]

	if eqir(before[:], order) == after: count += 1; dict["eqir"]= dict.get("eqir", []) + [order[0]]
	if eqri(before[:], order) == after: count += 1; dict["eqri"]= dict.get("eqri", []) + [order[0]]
	if eqrr(before[:], order) == after: count += 1; dict["eqrr"]= dict.get("eqrr", []) + [order[0]]
	
	if count >= 3:
		total += 1

	
dict2 = {}
solved = []
while len(dict2) < 16:	
	for key in dict.keys():	
		counted = Counter(dict[key])
		for fun in solved:
			del counted[fun]
		if len(counted) == 1:		
			for key1 in counted.keys():
				dict2[key1] = key
				solved.append(key1)

				
before = [0,0,0,0]

num_line += 2
for i in range(num_line, len(lines),1):
	fun, a,b,c = lines[i][:-1].split(" ")
	globals()[dict2[int(fun)]](before, [0,int(a),int(b),int(c)])
				
print total
print before














