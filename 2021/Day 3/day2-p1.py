def main(file):
    instructions = open(file, 'r')
    ls = instructions.readlines()
    instructions.close()
    for i in range(len(ls)):
        ls[i] = ls[i].split(' ')
        ls[i][1] = int(ls[i][1])
        
    depth = 0
    horizontal = 0

    for i in range(len(ls)):
        if ls[i][0] == 'forward':
            horizontal += ls[i][1]
        elif ls[i][0] == 'up':
            depth -= ls[i][1]
        elif ls[i][0] == 'down':
            depth += ls[i][1]

    return depth * horizontal

print(main("input.txt"))