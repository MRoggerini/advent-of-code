def get_up_scenic_score(grid, x, y):
    # how many trees the tree in x, y can see upward
    height = int(grid[x][y])
    score = 0
    # check all trees upward untill end or i find higher tree
    for i in range(x-1, -1, -1):
        if int(grid[i][y]) >= height:
            score+=1
            break
        score += 1
    return score


def get_down_scenic_score(grid, x, y):
    # how many trees the tree in x, y can see downward
    height = int(grid[x][y])
    score = 0
    # check all trees downward untill end or i find higher tree
    for i in range(x+1, len(grid[x])):
        if int(grid[i][y]) >= height:
            score+=1
            break
        score += 1
    return score


def get_left_scenic_score(grid, x, y):
    # how many trees the tree in x, y can see to the left
    height = int(grid[x][y])
    score = 0
    # check all trees to the left untill end or i find higher tree
    for i in range(y-1, -1, -1):
        if int(grid[x][i]) >= height:
            score+=1
            break
        score += 1
    return score


def get_right_scenic_score(grid, x, y):
    # how many trees the tree in x, y can see to the right
    height = int(grid[x][y])
    score = 0
    # check all trees to the right untill end or i find higher tree
    for i in range(y+1, len(grid)):
        if int(grid[x][i]) >= height:
            score+=1
            break
        score += 1
    return score


with open('day8_input.txt') as f:
    data = f.read().splitlines()

dim_row = len(data)
dim_col = len(data[0])

max_scenic_score = 0
visible = set()

for i in range(dim_row):
    for j in range(dim_col):
        # calculate the scenic scores for the current tree
        left_scenic_score = get_left_scenic_score(data, i, j)
        right_scenic_score = get_right_scenic_score(data, i, j)
        up_scenic_score = get_up_scenic_score(data, i, j)
        down_scenic_score = get_down_scenic_score(data, i, j)

        # one tree is visible if
        # - it is an edge tree, or
        # - its scenic score is equal to the distance to the edge and the edge
        #   tree is smaller than the current tree
        left_visible = left_scenic_score == j and (
                int(data[i][j]) > int(data[i][0]) or j == 0
            )
        right_visible = right_scenic_score == dim_col-1-j and (
                int(data[i][j]) > int(data[i][dim_col-1]) or j == dim_col-1
            )
        up_visible = up_scenic_score == i and (
                int(data[i][j]) > int(data[0][j]) or i == 0
            )
        down_visible = down_scenic_score == dim_row-1-i and (
                int(data[i][j]) > int(data[dim_row-1][j]) or i == dim_row-1
            )

        if left_visible or right_visible or up_visible or down_visible:
            # I used a set, since objects in set cannot be duplicated. If one
            # duplicate is added, the set doesn't change
            visible.add(f'{i:02}{j:02}')

        scenic_score = (
                left_scenic_score *
                right_scenic_score *
                up_scenic_score *
                down_scenic_score
            )
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score

print(f'# trees visible from the outside: {len(visible)}')
print(f'max scenic score for the grid: {max_scenic_score}')
