input_file = 'input.txt'
with open(input_file) as f:
    data = f.read().split('\n')[:-1]

occurrences = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def format_game(row):
    return [
        {
            pull.split(' ')[1]: int(pull.split(' ')[0])
            for pull in subset.split(', ')
        }
        for subset in row.split(': ')[1].split('; ')
    ]

def get_min_occurrences(game):
    min_occurrences = {i: 0 for i in ['red', 'green', 'blue']}
    for subset in game:
        for color, num in subset.items():
            if num > min_occurrences[color]:
                min_occurrences[color] = num

    return min_occurrences


def is_game_possible(min_occurrences):
    for color in min_occurrences.keys():
        if min_occurrences[color] > occurrences[color]:
            return False

    return True


possible_sum = 0
power_sum = 0

for i, row in enumerate(data):
    game = format_game(row)

    min_occurrences = get_min_occurrences(game)
    if is_game_possible(min_occurrences):
        possible_sum += i+1

    power = 1
    for num in min_occurrences.values():
        power *= num
    power_sum += power

print(f'Sum of possible game ids: {possible_sum}')
print(f'Sum of game power: {power_sum}')
