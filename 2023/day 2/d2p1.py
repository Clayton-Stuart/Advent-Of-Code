file = open('d2-input', 'r')
lines = file.readlines()
file.close()

for i in range(len(lines)):
    lines[i] = lines[i].split(": ")[1].strip().replace(';', ',').replace(', ', ',').split(',')
    for e in range(len(lines[i])):
        lines[i][e] = lines[i][e].split(' ')
        lines[i][e][0] = int(lines[i][e][0])


max_cubes = {
    'red': 12,
    'green': 13, 
    'blue': 14
}

num = 0

for i in range(len(lines)):
    cur_cubes = {
        'red': 0,
        'green': 0, 
        'blue': 0
    }

    for e in lines[i]:
        if cur_cubes[e[1]] < e[0]:
            cur_cubes[e[1]] = e[0]

    if max_cubes['red'] < cur_cubes['red'] or max_cubes['green'] < cur_cubes['green'] or max_cubes['blue'] < cur_cubes['blue']:
        pass
    else:
        num += (i+1)
print(num)
