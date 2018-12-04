import sys

file = open(sys.argv[1],'r')
text = file.readlines()
file.close()

text.sort()

current_id = 0
sleeping = {}  #total number of minutes sleeping
sleeping_minutes = {}  # number of times sleeping in each minute

for line in text:
	data = line.split(" ")[2]
	if data.startswith("G"): #Guard
		current_id = int(line.split(" ")[3][1:])
	elif data.startswith("f"): #falls
		minute_sleep_start = int((line.split(" ")[1][:-1]).split(":")[1]) #hh:mm
	elif data.startswith("w"): #wakes
		minute_slee_end = int((line.split(" ")[1][:-1]).split(":")[1]) #hh:mm
		sleep_duration = minute_slee_end - minute_sleep_start
		sleeping[current_id] = sleeping.get(current_id, 0) + sleep_duration	
		for minute in range(minute_sleep_start, minute_slee_end):
			sleeping_minutes[(current_id,minute)] = sleeping_minutes.get((current_id,minute),0) + 1
		
max_sleeping_duration = 0
max_sleeping_duration_id = 0
for id in sleeping.keys():		
	if sleeping[id] > max_sleeping_duration:
		max_sleeping_duration = sleeping[id]
		max_sleeping_duration_id = id

max_id_per_minute = 0	
most_minute_asleep = 0	

max_in_minute = 0
asleep_per_minute = 0
id_most_frequent = 0

for id,minute in sleeping_minutes.keys():
	if id == max_sleeping_duration_id:
		if sleeping_minutes[(id,minute)] > max_id_per_minute:
			max_id_per_minute = sleeping_minutes[(id,minute)]
			most_minute_asleep = minute
	if sleeping_minutes[(id,minute)] > asleep_per_minute:
		asleep_per_minute = sleeping_minutes[(id,minute)]
		id_most_frequent = id
		max_in_minute = minute

print "Guard with the most minutes asleep is ", max_sleeping_duration_id, ". He spends the most time asleep in minute ", most_minute_asleep 		
print "Multiplying gives ", max_sleeping_duration_id * most_minute_asleep

print "Guard ", id_most_frequent, "spent minute ", max_in_minute , "asleep more than any other guard"
print "Multiplying gives ",max_in_minute * id_most_frequent
