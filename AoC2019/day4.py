import sys

def check_num(number):
    adjacent = False
    for i in range(5):
        if( number[i] > number[i+1]): return False
        if( number[i] == number[i+1]): adjacent = True
    return adjacent


def part_two_check_num(number):
    adjacent = False
    i = 0
    while True:
        if( i >= 5): return adjacent
        if( number[i] > number[i+1]): return False
        count = 0
        while(i < 5 and number[i] == number[i+1]):
            count += 1
            i += 1
        if( count == 1): adjacent = True
        if( count == 0): i += 1


min = 245318
max = 765747

passwords_part1 = 0
passwords_part2 = 0

for number in range(min, max):
    test = False
    number = str(number)
    
    if( check_num(number)):
        passwords_part1 += 1
    if(part_two_check_num(number)):
        passwords_part2 += 1
    
    
    
print(passwords_part1)
print(passwords_part2)


