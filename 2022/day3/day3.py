def calculate_priority(letter):
    if ord(letter) - 97 < 0: # upper case letter
        return ord(letter) - 38 # - 65 + 27
    else: # lower case letter
        return ord(letter) - 96 # - 97 + 1


def add_badge(badge, letter, iteration, is_found):
    try:
        badge[letter].add(iteration)
        if len(badge[letter]) == 3 and not is_found:
            return (calculate_priority(letter), True)
    except KeyError:
        badge[letter] = {iteration}
    return (0, is_found)


with open('day3_input.txt') as f:
    data = f.readlines()

# A: 65
# a: 97

duplicates = []
tot_priority = 0
badge_priority = 0

for i, val in enumerate(data):
    if i%3 == 0: # start of a new group
        badge_elems = {}
        found = False

    chars = {}
    curr_len = len(val[:-1]) # exclude the \n at the end of each line
    for j in val[:int(curr_len/2)]:
        chars[j] = 1
        badge_value, found = add_badge(badge_elems, j, i%3, found)
        badge_priority += badge_value

    for j in val[int(curr_len/2):-1]:
        try:
            chars[j] += 1
            badge_value, found = add_badge(badge_elems, j, i%3, found)
            badge_priority += badge_value
            if chars[j] > 2: # ignore duplicated items in the second half
                continue
        except:
            badge_value, found = add_badge(badge_elems, j, i%3, found)
            badge_priority += badge_value
            continue
        duplicates.append(j)
        tot_priority += calculate_priority(j)


print(f'priority of the mixed up elements: {tot_priority}')
print(f'priority of the badges: {badge_priority}')
