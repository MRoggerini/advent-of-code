import re
import copy


with open('day5_input.txt') as f:
    data = f.readlines()

is_stack = True
stacks = {}
for i in data:
    if is_stack and i == '\n':
        # change reading mode from stack to instruction
        is_stack = False
        # we need to sort the dict since the fisrt created stacks are the taller
        stacks_9000 = dict(sorted(stacks.items()))
        stacks_9001 = copy.deepcopy(stacks_9000)
        continue
    elif is_stack:
        # reading of the starting stack model
        for j, val in enumerate(i[1:-1:4]):
            # only consider uppercase letters
            if re.match(r"[A-Z]", val):
                try:
                    stacks[j+1].insert(0,val)
                except KeyError:
                    stacks[j+1] = [val]
    else:
        moves = [int(j) for j in re.findall(r'\d+', i)]
        # movement for CrateMover 9000: crates are moved one by one
        for j in range(moves[0]):
            stacks_9000[moves[2]].append(stacks_9000[moves[1]].pop(-1))

        # movement for CrateMover 9001: crates are moved together
        # copy all crates from one stack to the other
        stacks_9001[moves[2]] += stacks_9001[moves[1]][-moves[0]:]
        # remove crates from starting stack
        stacks_9001[moves[1]] = stacks_9001[moves[1]][:-moves[0]]

top_crates_9000 = ''.join([v[-1] for k, v in stacks_9000.items()])
top_crates_9001 = ''.join([v[-1] for k, v in stacks_9001.items()])
print(f'crates on top of each stack with CrateMover 9000: {top_crates_9000}')
print(f'crates on top of each stack with CrateMover 9001: {top_crates_9001}')
