# Day 3: Part One

import re

file = open('day3-1.txt', 'r')
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

matches = re.findall(pattern, file.read())

result = 0
for match in matches:
    result += (int(match[0]) * int(match[1]))

print(result)