def getIncreasedSums(file):
    ls = open(file, 'r')
    ints = ls.readlines()
    ls.close()
    for i in range(len(ints)):
        ints[i] = int(ints[i])
    amount = 0
    sums = []
    for i in range(len(ints) - 2):
        sums.append(ints[i] + ints[i+1] + ints[i+2])
    for i in range(len(sums)):
        if i == 0:
            pass
        else:
            if sums[i] > sums[i - 1]:
                amount += 1
    return amount

print(getIncreasedSums('input.txt'))