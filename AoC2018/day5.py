import sys

def lenght(text):
	changed = True
	while(changed == True):
		changed = False
		i = 0
		while( i < len(text)-1):
			if abs(ord(text[i+1]) - ord(text[i])) == 32:
				changed = True
				text = text[:i] + text[i+2:]
			i += 1
	return len(text)

file = open(sys.argv[1],'r')
text = file.readline()
file.close()

text2 = text

print lenght(text)


best = len(text2)
letter_remove = ""
letters = []
for letter in text2:
	if letter.lower() not in letters:
		letters.append(letter.lower())
	
for letter in letters:
	text = text2
	text = text.replace(letter,"")
	text = text.replace(letter.upper(),"")
	score = lenght(text)
	if score < best:
		best = score
		letter_remove = letter

print best, letter_remove





