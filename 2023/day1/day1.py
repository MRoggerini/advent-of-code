import re


with open('input.txt') as f:
    data = f.read().split('\n')[:-1]

text_to_number = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

numbers_part1 = []
numbers_part2 = []

word_numbers = 'one two three four five six seven eight nine'

numbers_regex = f'\\d'
# use lookahead to allow the substitution of 'twone' to '2'+'1'
word_numbers_regex = f'(?=({word_numbers.replace(" ", "|")}|\\d))'


def word_to_num(word):
    try:
        return text_to_number[word]
    except KeyError:
        return word


for row in data:
    number_part1 = re.findall(numbers_regex, row)
    first = number_part1[0]
    last = number_part1[-1]
    number_part1 = int(f'{first}{last}')
    numbers_part1.append(number_part1)

    number_part2_token = re.findall(word_numbers_regex, row)
    first = word_to_num(number_part2_token[0])
    last = word_to_num(number_part2_token[-1])
    number_part2 = int(f'{first}{last}')
    numbers_part2.append(number_part2)

print(f'solution to first part: {sum(numbers_part1)}')
print(f'solution to second part: {sum(numbers_part2)}')
