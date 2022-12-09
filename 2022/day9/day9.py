def move_up(position):
    position[0] -= 1

def move_down(position):
    position[0] += 1

def move_left(position):
    position[1] -= 1

def move_right(position):
    position[1] += 1

# move defines a compact way to represent the possible movements and apply them
move = {
        'U': move_up,
        'D': move_down,
        'L': move_left,
        'R': move_right
    }

def move_t(val, dist):
    # how to move knot based on movement of previous knot
    # we both do hotizontal and vertical movement in each case:
    # if both distance is > 0, we certainly need to do a diagonal movement
    # else we will only operate an horizontal/vertical movement
    if dist[0] > 0:
        move['D'](val)
    elif dist[0] < 0:
        move['U'](val)

    if dist[1] > 0:
        move['R'](val)
    elif dist[1] < 0:
        move['L'](val)


with open('day9_input.txt') as f:
    data = f.read().splitlines()

num_knots = 10
visited = {i:set() for i in range(num_knots)}
rope_pos = {i:[0,0] for i in range(num_knots)} # [row, col]
# add starting position as visited for all knots
for k,v in visited.items():
    v.add('0:0')

for i in data:
    direction = i[0]
    cardinality = int(i[2:])
    for j in range(cardinality):
        for k, val in rope_pos.items():
            if k == 0: # head always move
                move[direction](val)
                visited[k].add(f'{val[0]}:{val[1]}')
            else:
                # other knots only move if previous knot has a Cebysev distance
                # greater than 1
                # Cebysev distance: the king's distance, the number of moves a
                # king in chess must do to move from A to B
                curr_dist = [
                        rope_pos[k-1][0] - rope_pos[k][0],
                        rope_pos[k-1][1] - rope_pos[k][1]
                    ]
                if max(abs(curr_dist[0]), abs(curr_dist[1])) > 1:
                    move_t(val, curr_dist)
                    visited[k].add(f'{val[0]}:{val[1]}')
                else:
                    # if this knot did not move, the next one will not move,
                    # since it is already ad Cebysev distance <= 1
                    break

for k, v in visited.items():
    print(f'Locations visited by knot {k}: {len(v)}')
