# Day 1: Part Two

with open('day1-2.txt', 'r') as file:
    lines = [tuple(map(int, line.split())) for line in file]

line1, line2 = zip(*lines)
line1 = sorted(line1)
line2 = sorted(line2)
counts = {}
for item in line2:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

result = 0
for item in line1:
    if item in counts:
        result += item * counts[item]

print(result)



