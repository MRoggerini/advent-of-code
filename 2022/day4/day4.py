import re


with open('day4_input.txt') as f:
    data = f.readlines()

total_overlap = 0
partial_overlap = 0
for i, val in enumerate(data):
    # extract the values from the string (as integers)
    elf1_l, elf1_h, elf2_l, elf2_h = [int(j) for j in re.findall('\d+', val)]
    if (elf1_l - elf2_l) * (elf2_h - elf1_h) >= 0:
        total_overlap += 1
    if (elf1_h >= elf2_l) and (elf1_l <= elf2_l) or (elf2_h >= elf1_l) and (elf2_l <= elf1_l):
        partial_overlap += 1

print(f'total number of totally overlapping sections: {total_overlap}')
print(f'total number of partially overlapping sections: {partial_overlap}')
