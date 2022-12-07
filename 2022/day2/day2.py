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


# get the input data
with open('day2_input.txt') as f:
    data = f.readlines()

score_pt1 = []
tot_score_pt1 = 0
score_pt2 = []
tot_score_pt2 = 0

for i in data:
    col1 = move_score[i[0]] # the move of our challenger
    col2 = move_score[i[2]] # pt1: our move; pt2: the desired outcome

    # we get the score of the strategy in pt1
    curr_score_pt1 = game_matrix_pt1[col2][col1]
    score_pt1.append(curr_score_pt1)
    tot_score_pt1 += curr_score_pt1

    # we get the score of the strategy in pt2
    curr_score_pt2 = game_matrix_pt2[col2][col1]
    score_pt2.append(curr_score_pt2)
    tot_score_pt2 += curr_score_pt2

print(f'grand total with part 1 strategy: {tot_score_pt1}')
print(f'grand total with part 2 strategy: {tot_score_pt2}')
