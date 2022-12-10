with open('day10_input.txt') as f:
    data = f.read().splitlines()

x = 1
clocks = []
for i in data:
    if i == 'noop':
        # noop does nothing for one cycle
        clocks.append(x)
    else:
        # addx add the input value after the completion of 2 cycles
        clocks.append(x)
        clocks.append(x)
        x += int(i[5:])

signal_strenght = [(i+1)*val for i, val in enumerate(clocks)]
print(f'the signal strenght is {sum(signal_strenght[19::40])}')

for i, val in enumerate(clocks):
    if i%40==0:
        # carriage return
        print()
    # print character only if the current position is under the sprite
    print('#' if val-1<=i%40 and i%40<=val+1 else ' ', end='')
