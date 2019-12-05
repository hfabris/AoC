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


file = open("day19.txt","r")
lines = []
ip = int(file.readline().split(" ")[1])

print ip

registers = [0,0,0,0,0,0]

for line in file.readlines():
	if line.startswith("#"):
		ip = int(file.readline().split(" ")[1])
	else:
		lines.append(line.strip())
	
file.close()

while registers[ip] < len(lines):
	fun, a,b,c = lines[registers[ip]].split(" ")
	globals()[fun](registers, [0,int(a),int(b),int(c)])
	registers[ip] += 1

print registers[0]




















