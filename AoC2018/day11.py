import sys

def get_power(x,y):
	power = 0
	
	rack_id = x+10
	power = rack_id * y + serial
	power *= rack_id
	power = power % 1000 / 100 - 5
	return power
	

grid = {}
serial = 6548

for x in range(1,301):
	for y in range(1,301):
		grid[(x,y)] = get_power(x,y)
		
summed_table = {}

for x in range(1,301):
	for y in range(1,301):
		summed_table[(x,y)] = grid[(x,y)] + summed_table.get((x,y-1),0) + summed_table.get((x-1,y),0) - summed_table.get((x-1,y-1),0)
		

power_max = 0
coord_max = ()		
for x in range(1,301):
	for y in range(1,301):
		for size in range(1, 301 - max(x,y)):
			k = summed_table[(x,y)] - summed_table[(x,y+size)] - summed_table[(x+size,y)] + summed_table[(x+size,y+size)]
			if k > power_max:
				power_max = k
				coord_max = (x+1,y+1,size)
		
print coord_max, power_max		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		