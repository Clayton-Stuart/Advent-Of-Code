file = open('d2-input', 'r')
lines = file.readlines()
file.close()

for i in range(len(lines)):
    lines[i] = lines[i].split(": ")[1].strip().replace(';', ',').replace(', ', ',').split(',')
    for e in range(len(lines[i])):
        lines[i][e] = lines[i][e].split(' ')
        lines[i][e][0] = int(lines[i][e][0])

num = 0

for i in range(len(lines)):
    rel_min = {
        'red': 0,
        'green': 0, 
        'blue': 0
    }

    for e in lines[i]:
        if e[0] > rel_min[e[1]]:
            rel_min[e[1]] = e[0]

    num += (rel_min['red'] * rel_min['green'] * rel_min['blue'])


print(num)    
