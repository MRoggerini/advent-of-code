import re
import copy


class Monkey:
    def __init__(self):
        self.items = []
        self.operation = ''
        self.test_case = None
        self.true_monkey = None
        self.false_monkey = None
        self.monkey_business = 0
        self.worry_divisor = 1
        self.common_multiplier = 1


    def update_values(self):
        items = []
        for i in self.items:
            current = eval(self.operation.replace('old', str(i)))
            current = current // self.worry_divisor
            # we only keep the interesting part, needed to check conditions
            # if we didn't, the numbers would explode in very big and
            # non-manageable numbers
            current %= self.common_multiplier
            items.append(current)
        self.items = items
        self.monkey_business += len(self.items)


    def pass_items(self):
        starting_items = [i for i in self.items]
        for i in starting_items:
            if i % self.test_case == 0:
                self.true_monkey.items.append(i)
            else:
                self.false_monkey.items.append(i)
            self.items.remove(i)


    def monkey_game(self):
        self.update_values()
        self.pass_items()


def get_monkey_business(rounds, monkeys, worry_divisor):
    for monkey in monkeys:
        monkey.worry_divisor = worry_divisor

    for i in range(rounds):
        for monkey in monkeys:
            monkey.monkey_game()

    # same concept of challenge of day 1:
    #  - insert the new number in the correct position in the array
    #  - keep only the n biggest numbers of the array
    tot_max_monkeys = 2
    max_monkeys = [0 for i in range(tot_max_monkeys)]
    for monkey in monkeys:
        pos = 0
        for j in max_monkeys:
            if monkey.monkey_business < j:
                break
            pos+=1
        max_monkeys.insert(pos, monkey.monkey_business)
        max_monkeys = max_monkeys[1:]

    tot_monkey_business = 1
    for i in max_monkeys:
        tot_monkey_business *= i

    print(f'level of monkey business after {rounds} rounds: {tot_monkey_business}')


with open('day11_input.txt') as f:
    data = f.read().splitlines()

monkeys = [Monkey() for i in range((len(data)+1)//7)]
common_multiplier = 1

current_monkey = 0
for i in data:
    if 'Monkey' in i:
        current_monkey = int(re.findall(r'\d+', i)[0])
    elif 'Starting items' in i:
        monkeys[current_monkey].items = [int(j) for j in re.findall(r'\d+', i)]
    elif 'Operation' in i:
        monkeys[current_monkey].operation = i.split('=')[-1]
    elif 'Test' in i:
        monkeys[current_monkey].test_case = int(re.findall(r'\d+', i)[0])
        common_multiplier *= int(re.findall(r'\d+', i)[0])
    elif 'If true' in i:
        true_monkey_index = int(re.findall(r'\d+', i)[0])
        monkeys[current_monkey].true_monkey = monkeys[true_monkey_index]
    elif 'If false' in i:
        false_monkey_index = int(re.findall(r'\d+', i)[0])
        monkeys[current_monkey].false_monkey = monkeys[false_monkey_index]

for monkey in monkeys:
    monkey.common_multiplier = common_multiplier

get_monkey_business(20, copy.deepcopy(monkeys), 3)
get_monkey_business(10000, copy.deepcopy(monkeys), 1)
