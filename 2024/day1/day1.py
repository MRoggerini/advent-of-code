

with open('input.txt') as f:
    data = f.read().split('\n')[:-1]

column1 = []
column2 = []
place_occurrence = {}

for i in data:
    c1_data = int(i.split()[0])
    c2_data = int(i.split()[-1])

    column1.append(c1_data)
    column2.append(c2_data)

    try:
        place_occurrence[c2_data] += 1
    except KeyError:
        place_occurrence[c2_data] = 1


column1.sort()
column2.sort()

distance = 0
occurrence = 0

for i in range(len(column1)):
    c1_data = column1[i]
    c2_data = column2[i]
    distance += abs(c1_data - c2_data)

    try:
        c1_occurrence = place_occurrence[c1_data]
    except KeyError:
        c1_occurrence = 0
    occurrence += (c1_data * c1_occurrence)


print(f'Total distance is: {distance}')
print(f'Total occurrence is: {occurrence}')
