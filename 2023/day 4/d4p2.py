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

cards = {}
cards_copies = {}

for i in range(len(lines)):
    cards[i + 1] = lines[i]
    cards_copies[i + 1] = 1

for key in cards.keys():
    line = cards[key]
    matches = 0
    for i in line[0]:
        if i in line[1]:
                matches += 1

    for i in range(matches):
        cards_copies[key + i + 1] += cards_copies[key]

num = 0
for key in cards_copies.keys():
    num += cards_copies[key]

print(num)