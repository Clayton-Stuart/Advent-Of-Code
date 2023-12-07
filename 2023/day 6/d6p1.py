file = open('d6-input', 'r')
lines = file.readlines()
file.close()

for i in range(len(lines)):
    lines[i] = list(map(int, lines[i].strip().replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(':', '').split(' ')[1:]))

pairings = {}

for i in range(len(lines[0])):
    pairings[lines[0][i]] = lines[1][i]

methods = []

for key in pairings.keys():
    methods.append(0)
    sets = {}
    for hold in range(key + 1):
        sets[hold] = hold * (key - hold)

    record = pairings[key]

    for key2 in sets.keys():
        if sets[key2] > record:
            methods[-1] += 1

print(methods[0] * methods[1] * methods[2] * methods[3])
    