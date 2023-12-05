import re
import json


# in_file = 'test_input.txt'
in_file = 'input.txt'

with open(in_file) as f:
    data = f.read().split('\n')[:-1]

num_match = r'\d+'
gear_match = r'\*'
symbol_match = r'[^\.\d]'

elem_match = f'{num_match}|{gear_match}|{symbol_match}'

# key: x_s:x_e;y
numbers = {}
gears = {}
symbols = {}

part_numbers = {}
gear_numbers = []

def find_match(text, regex, line, add_to):
    for symbol in re.finditer(regex, text):
        _id = len(add_to.keys())
        for x in range(symbol.start(), symbol.end()):
            add_to[f'{x};{line}'] = (_id, symbol.group())

for i, row in enumerate(data):
    find_match(row, num_match, i, numbers)
    find_match(row, symbol_match, i, symbols)


for pos, sym in symbols.items():
    curr_gear = {}
    x = int(pos.split(';')[0])
    y = int(pos.split(';')[1])
    for x_d in range(-1,2):
        for y_d in range(-1,2):
            try:
                num = numbers[f'{x+x_d};{y+y_d}']
            except KeyError:
                continue
            part_numbers[num[0]] = int(num[1])
            if sym[1] == '*':
                curr_gear[num[0]] = int(num[1])
    try:
        g1, g2 = list(curr_gear.values())
    except Exception as e:
        continue
    gear_ratio = g1 * g2

    gear_numbers.append(gear_ratio)

print(f'Sum of all part numbers: {sum(part_numbers.values())}')
print(f'Sum of all gear ratios:  {sum(gear_numbers)}')
