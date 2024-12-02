# Day 2: Part One

with open('day2-1.txt', 'r') as file:
    lines = [tuple(map(int, line.split())) for line in file]

def is_safe_trend(values):
    for i in range(len(values) - 1):
        diff = values[i + 1] - values[i]
        #Difference between to neighbor values out of range
        if not (-3 <= diff <= 3) or diff == 0:
            return 0
        #Checking if trend changes
        if i > 0:
            prev_diff = values[i] - values[i - 1]
            if (prev_diff > 0 and diff < 0) or (prev_diff < 0 and diff > 0):
                return 0

    return 1

result = 0
for reports in lines:
    if is_safe_trend(reports) == 1:
        result += 1

print(result)