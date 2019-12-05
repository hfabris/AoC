def is_subseq(v2, v1):
	for x,y in zip(v1,v2):
		if x != y:
			return False
	return True
		
		
input = 640441
first = 3
second = 7

first_num = 0
second_num = 1
input_to_list = input

list_input = []
while input_to_list > 0:
	list_input.append(input_to_list % 10)
	input_to_list /= 10

list_input.reverse()	
print list_input
list = [first, second]

while True:
	new = first + second
	if new >=10:
		list.append(new / 10)
		if is_subseq(list[-len(list_input):], list_input):
			print len(list) - len(list_input)
			break
	list.append(new % 10)
	if is_subseq(list[-len(list_input):], list_input):
			print len(list) - len(list_input)
			break
	first_num = (1+first+first_num) % len(list) 
	second_num = (1+second+second_num) % len(list) 
	
	first = list[first_num]
	second = list[second_num] 
	







