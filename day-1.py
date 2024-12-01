# Day 1: Part One

with open('day1-1.txt', 'r') as file:
    lines = [tuple(map(int, line.split())) for line in file]

line1, line2 = zip(*lines)

line1 = sorted(line1)
line2 = sorted(line2)

result = sum(abs(a - b) for a, b in zip(line1, line2))

print(result)
