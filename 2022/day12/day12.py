def check_up(x, y, data, visited):
    if (x-1, y) in visited:
        return False
    if x < 1 or y < 0:
        return False
    try:
        if data[x-1][y] >= data[x][y]-1:
            return True
        return False
    except IndexError:
        return False


def check_down(x, y, data, visited):
    if (x+1, y) in visited:
        return False
    if x < 0 or y < 0:
        return False
    try:
        if data[x+1][y] >= data[x][y]-1:
            return True
        return False
    except IndexError:
        return False


def check_left(x, y, data, visited):
    if (x, y-1) in visited:
        return False
    if x < 0 or y < 1:
        return False
    try:
        if data[x][y-1] >= data[x][y]-1:
            return True
        return False
    except IndexError:
        return False


def check_right(x, y, data, visited):
    if (x, y+1) in visited:
        return False
    if x < 0 or y < 0:
        return False
    try:
        if data[x][y+1] >= data[x][y]-1:
            return True
        return False
    except IndexError:
        return False


with open('day12_input.txt') as f:
    data = f.read().splitlines()

start = set()

for i, row in enumerate(data):
    curr_row = []
    for j, elem in enumerate(row):
        curr_row.append(ord(elem)-97)
        if elem == 'a' or elem == 'S':
            start.add((i, j))
        if elem == 'S':
            start_x, start_y = (i, j)
        if elem == 'E':
            end_x, end_y = (i, j)
    data[i] = curr_row

data[end_x][end_y] = 25
data[start_x][start_y] = 0

visited = set()
to_expand = {(end_x, end_y)}
# matrix telling the distance from the end
distance = [[float('inf') for j in i] for i in data]
# end is distant 0 from end
distance[end_x][end_y] = 0

current_distance = 1
while len(to_expand) > 0:
    # for each cell starting from the end, we update the distance from the end
    to_expand_next = set()
    for current in to_expand:
        # add to visited not to check already visited cells
        visited.add(current)
        x, y = current
        if check_up(x, y, data, visited):
            distance[x-1][y] = current_distance
            to_expand_next.add((x-1, y))
        if check_down(x, y, data, visited):
            distance[x+1][y] = current_distance
            to_expand_next.add((x+1, y))
        if check_left(x, y, data, visited):
            distance[x][y-1] = current_distance
            to_expand_next.add((x, y-1))
        if check_right(x, y, data, visited):
            distance[x][y+1] = current_distance
            to_expand_next.add((x, y+1))

    to_expand = to_expand_next

    current_distance += 1

print(f'distance from start to destination: {distance[start_x][start_y]}')
min_distance = min([distance[i[0]][i[1]] for i in start])
print(f'min distance from spot with height "a" and destination: {min_distance}')
