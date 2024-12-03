# Day 3: Part Two

import re

file = open('day3-2.txt', 'r').read()
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
do_active = True
matches = []
end = 0
for match in re.finditer(pattern, file, re.DOTALL):
    snippet = file[end:match.start()]
    end = match.end()
    if "don't()" in snippet and do_active:
        do_active = False
    if "do()" in snippet and not do_active:
        do_active = True
    if do_active:
        do_match = re.findall(pattern,match.group(0))
        matches.append(do_match)
result = 0
for match in matches:
    result += (int(match[0][0]) * int(match[0][1]))
print(result)