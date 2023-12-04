file = open('d4-input', 'r')
lines = file.readlines()
file.close()


for i in range(len(lines)):
    lines[i] = lines[i].strip()
    lines[i] = lines[i].replace('  ', ' ')
    lines[i] = lines[i].split(': ')[1]
    lines[i] = lines[i].split(' | ')
    lines[i][0] = list(map(int, lines[i][0].split(' ')))
    lines[i][1] = list(map(int, lines[i][1].split(' ')))
    
num = 0

for i in lines:
    cur = 0
    for e in i[0]:
        if e in i[1]:
            if cur == 0:
                cur += 1
            else:
                cur *= 2

    num += cur


print(num)

