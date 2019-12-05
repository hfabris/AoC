def runGenerations(rules, plants, iterations):
	for generation in range(iterations):	
		lowestPlant = min(plants)
		highestPlant = max(plants)
		lastPossible = highestPlant - lowestPlant + 7
		pots = ''.join(['#' if i in plants else '.' for i in range(lowestPlant - 4, highestPlant + 5)])
		plants = []
		for i in range(2, lastPossible):
			if rules[pots[i-2:i+3]]:
				plants.append(i - 4 + lowestPlant)
	return sum(plants)

with open('day12.txt') as inFile:
	lines = inFile.read().splitlines()
	plants = [i for i, c in enumerate(lines[0][15:]) if c == "#"]
	rules = dict((line[:5], line[9] == "#") for line in lines[2:])

print('Part 1:', runGenerations(rules, plants, 20))
print('Part 2:', runGenerations(rules, plants, 300) + ((50000000000 - 300) * 45))