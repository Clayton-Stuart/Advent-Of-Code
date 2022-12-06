file = open('input.txt', 'r')
ls = file.readlines()
file.close()

for i in range(len(ls)):
    ls[i] = ls[i].strip().split(',')
    ls[i][0] = ls[i][0].split('-')
    ls[i][1] = ls[i][1].split('-')

for i in range(len(ls)):
    for e in range(len(ls[i])):
        for j in range(len(ls[i][e])):
            ls[i][e][j] = int(ls[i][e][j])

count = 0
for i in range(len(ls)):
    if (ls[i][0][0] >= ls[i][1][0] and ls[i][0][0] <= ls[i][1][1]) or (ls[i][0][1] >= ls[i][1][0] and ls[i][0][1] <= ls[i][1][1]) or (ls[i][1][0] >= ls[i][0][0] and ls[i][1][0] <= ls[i][0][1]) or (ls[i][1][1] >= ls[i][0][0] and ls[i][1][1] <= ls[i][0][1]):
        count += 1

print(count)