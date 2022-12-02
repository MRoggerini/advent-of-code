
move = {
        'A': 0,
        'B': 1,
        'C': 2,
        'X': 0,
        'Y': 1,
        'Z': 2
    }

point_outcome: {
        'X': 0,
        'Y': 3,
        'Z': 6
    }

# rows: our play
# columns: their play
# cell: the score of the selected play
game_matrix_pt1 = [
        #A    B    C
        [3+1, 0+1, 6+1],#X
        [6+2, 3+2, 0+3],#Y
        [0+3, 6+3, 3+3] #Z
    ]

# rows: desired output X loss, Y tie, Z win
# columns: their play
# cell: the score of the selected play
game_matrix_pt2 = [
        #A,   B,   C
        [0+3, 0+1, 0+2],#X
        [3+1, 3+2, 3+3],#Y
        [6+2, 6+3, 6+1] #Z
    ]


with open('day2_input.txt') as f:
    data = f.readlines()

score_pt1 = []
score_pt2 = []

for i in data:
    col1 = move[i[0]] # the move of our challenger
    col2 = move[i[2]] # pt1: our move; pt2: the outcome to obtain

    curr_score_pt1 = game_matrix_pt1[col2][col1]
    curr_score_pt2 = game_matrix_pt2[col2][col1]
    score_pt1.append(curr_score_pt1)
    score_pt2.append(curr_score_pt2)

print(f'grand total with part 1 strategy: {sum(score_pt1)}')
print(f'grand total with part 2 strategy: {sum(score_pt2)}')
