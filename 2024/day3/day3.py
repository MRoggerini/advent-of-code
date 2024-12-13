import re


with open('input.txt') as f:
    data = f.read().split('\n')[:-1]

total = 0
conditional_total = 0

is_enabled = True
for i in data:
    mults = re.findall(r'mul\(\d+,\d+\)', i)
    conditional_mults = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", i)
    for mul in mults:
        numbers = re.findall(r'\d+', mul)
        total += int(numbers[0]) * int(numbers[1])

    for cond in conditional_mults:
        if 'do' in cond:
            is_enabled = 'do()' == cond
        elif is_enabled:
            numbers = re.findall(r'\d+', cond)
            conditional_total += int(numbers[0]) * int(numbers[1])

print(f'Multiplication total: {total}')
print(f'Conditional multiplication total: {conditional_total}')
