import re


# in_file = 'test_input.txt'
in_file = 'input.txt'

with open(in_file) as f:
    data = f.read().split('\n')[:-1]

win_list = []
win_match = []

for row in data:
    num = row.split(':')[1]
    winning_num_raw, my_num_raw = num.split('|')

    winning_num = set(re.findall(r'\d+', winning_num_raw))
    my_num = set(re.findall(r'\d+', my_num_raw))

    match = len(my_num.intersection(winning_num))
    win_match.append(match)

    if match == 0:
        win_list.append(0)
    else:
        win_list.append(2**(match-1))

print(f'Amount won: {sum(win_list)}')

ticket_copies = [1 for i in win_match]

for i, win_amount in enumerate(win_match):
    curr_amount = ticket_copies[i]
    for j in range(i+1, i+1+win_amount):
        ticket_copies[j]+=curr_amount

print(f'Total number of tickets: {sum(ticket_copies)}')
