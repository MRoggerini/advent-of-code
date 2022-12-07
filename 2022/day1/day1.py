with open('day1_input.txt') as f:
    data = f.readlines()

elfs = []
curr = 0
tot_max_elfs = 3
max_elf = [0 for i in range(tot_max_elfs)]

for i in data:
    try:
        curr += float(i[:-1])
    except:
        elfs.append(curr)
        pos = 0
        # the idea is to insert the elf in the correct position among the
        # top n elfs, and then drop the elf with less calories
        for j, val in enumerate(max_elf):
            if curr<val:
                break
            else:
                pos+=1
        max_elf.insert(pos, curr)
        max_elf = max_elf[1:]
        curr = 0

print(f'top {tot_max_elfs} elfs: {max_elf}')
print(f'elf with more calories: {max_elf[-1]}')
print(f'sum of the calories of the top {tot_max_elfs} elfs: {sum(max_elf)}')
