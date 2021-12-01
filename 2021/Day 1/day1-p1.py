def getIncreased(file):
    ls = open(file, 'r')
    ints = ls.readlines()
    ls.close()
    for i in range(len(ints)):
        ints[i] = int(ints[i])
    amount = 0
    for i in range(len(ints)):
        if i == 0:
            pass
        else:
            if ints[i] > ints[i - 1]:
                amount += 1
    return amount
    

print(getIncreased('input.txt'))