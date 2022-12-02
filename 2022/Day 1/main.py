file = open('input.txt', 'r')
lines = file.readlines()
file.close()

elves = [0]
for i in lines:
    if i != '\n':
        elves[-1] += int(i.strip())
    else:
        elves.append(0)

def part1(elves):
    largest = elves[0]
    for i in range(1, len(elves)):
        if elves[i] > largest:
            largest = elves[i]
    print(largest)

def part2(elves):
    top = []
    for _ in range(3):
        largest = elves[0]
        index = 0
        for i in range(1, len(elves)):
            if elves[i] > largest:
                largest = elves[i]
                index = i
        top.append(elves[index])
        elves.pop(index)
    print(sum(top))

part1(elves)
part2(elves)

            
