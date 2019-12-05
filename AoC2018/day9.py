import sys, numpy

file = open(sys.argv[1],'r')
text = file.readline()
file.close()


players = int(text.split(" ")[0])
last_worth = int(text.split(" ")[6])
# players = 13
# last_worth = 7999

last_worth *= 100

marbles = [0]
score = numpy.zeros(players)
current_marble = 0
current_player = 0

for i in range(1,last_worth):
	if i % 23 == 0:
		score[current_player-1] += i
		counter_clockwise = (len(marbles) + current_marble - 7) % len(marbles)
		score[current_player-1] += marbles.pop(counter_clockwise)
		current_player = (current_player) % players + 1
		current_marble = counter_clockwise
	else:
		marbles.insert((current_marble+1) % len(marbles)+1, i)
		current_player = (current_player) % players + 1
		current_marble = marbles.index(i)

max_score = max(score)
print int(max_score)









