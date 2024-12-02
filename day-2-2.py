# Day 2: Part Two

with open('day2-2.txt', 'r') as file:
    lines = [tuple(map(int, line.split())) for line in file]

def is_safe_trend(values):
    for i in range(len(values) - 1):
        diff = values[i + 1] - values[i]
        # Difference between to neighbor values out of range
        if not (-3 <= diff <= 3) or diff == 0:
            return False
        # Checking if trend changes
        if i > 0:
            prev_diff = values[i] - values[i - 1]
            if (prev_diff > 0 and diff < 0) or (prev_diff < 0 and diff > 0):
                return False

    return True

def is_safe_with_removal(values):

    if is_safe_trend(values):
        return True

    #Checking safe status by removing elements
    for i in range(len(values)):
        modified_values = values[:i] + values[i + 1:]
        if is_safe_trend(modified_values):
            return True

    return False

result = 0
for reports in lines:
    if is_safe_with_removal(reports):
        result += 1

print(result)
