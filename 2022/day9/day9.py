def move_up(position):
    position[0] -= 1

def move_down(position):
    position[0] += 1

def move_left(position):
    position[1] -= 1

def move_right(position):
    position[1] += 1

def stay(position):
    pass

# move defines a compact way to represent the possible movements and apply them
move = {
        'U': move_up,
        'D': move_down,
        'L': move_left,
        'R': move_right,
        '0': stay
    }



with open('day9_input.txt') as f:
    data = f.read().splitlines()

visited_tail = set()
h_pos = [0, 0] # [row, col]
t_pos = [0, 0] # [row, col]

for i in data:
    direction = i[0]
    cardinality = int(i[2:])
    for j in range(cardinality):
        move[direction](h_pos)
        curr_dist = [h_pos[0] - t_pos[0], h_pos[1] - t_pos[1]]
        manh_dist = abs(curr_dist[0]) + abs(curr_dist[1])
        if max(abs(curr_dist[0]), abs(curr_dist[1])) > 1:
            if manh_dist == 2:

print(h_pos)
