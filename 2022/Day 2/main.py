file = open('input.txt', 'r')
lines = file.readlines()
file.close()

translations = {'a': 1, 'b': 2, 'c': 3, 'x': 1, 'y': 2, 'z': 3}

for i in range(len(lines)):
    lines[i] = [translations[lines[i].strip().lower().split(' ')[0]], translations[lines[i].strip().lower().split(' ')[1]]]
    

def part1(lines):
    game_states = [['11', '22', '33'], ['12', '23', '31'], ['13', '21', '32']] # tie win lose
    score = 0
    for i in lines:
        score += i[1]
        if str(i[0]) + str(i[1]) in game_states[0]:
            score += 3
        elif str(i[0]) + str(i[1]) in game_states[1]:
            score += 6
    return score


def part2(lines):
    win = {1: 2, 2: 3, 3: 1}
    lose = {1: 3, 3: 2, 2: 1}
    score = 0
    for i in lines:
        if i[1] == 2:
            score += 3
            score += i[0]
        if i[1] == 3:
            score += 6
            score += win[i[0]]
        if i[1] == 1:
            score += lose[i[0]]
    return score


print(part1(lines))
print(part2(lines))
