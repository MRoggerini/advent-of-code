

with open('input.txt') as f:
    data = f.read().split('\n')[:-1]


def is_safe(level):
    sorted_level = sorted(level)
    reversed_level = list(reversed(level))

    if sorted_level != level and sorted_level != reversed_level:
        return False

    for i in range(len(level) - 1):
        distance = abs(level[i] - level[i+1])
        if distance == 0 or distance > 3:
            return False

    return True


def is_safe_dampened(level):
    for i in range(len(level)):
        new_level = level[0:i] + level[i+1:]
        if is_safe(new_level):
            return True
    return False


tot_safe = 0
tot_safe_dampened = 0

for i in data:
    level = [int(j) for j in i.split()]
    if is_safe(level):
        tot_safe += 1
        tot_safe_dampened += 1
    elif is_safe_dampened(level):
        tot_safe_dampened += 1


print(f'total safe levels: {tot_safe}')
print(f'total safe levels after dampening: {tot_safe_dampened}')
