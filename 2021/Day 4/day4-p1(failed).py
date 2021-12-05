def main(file):
    # Extract data from file
    document = open(file)
    ls = document.readlines()
    document.close()

    # Get numbers list
    bingoNumString = ls[0]
    bingoNums = bingoNumString.split(',')
    for i in range(len(bingoNums)):
        bingoNums[i] = int(bingoNums[i])

    # Get bingo boards
       
    ls.pop(0)
    ls.pop(0)
    boards = [[]]
    midStr = ''
    for i in range(len(ls)):
        midStr = ls[i].split(' ')
        
        for e in range(midStr.count('')):
            midStr.remove('')
        
        if midStr != ['\n']:
            boards[-1].append(midStr)
        else:
            boards.append([])

    # Set board values from string to int
    for i in range(len(boards)):
        for e in range(len(boards[i])):
            for u in range(len(boards[i][e])):
                boards[i][e][u] = int(boards[i][e][u])

    # Play Game
    for i in range(len(bingoNums)):
        for e in range(len(boards)):
            for u in range(len(boards[e])):
                for a in range(len(boards[e][u])):
                    if boards[e][u][a] == bingoNums[i]:
                        boards[e][u][a] = 'fill'
                    
                        # Check for bingo
                        # check horizontal
                        for j in range(len(boards)):
                            if boards[j].count('fill') == 5:
                                count = 0
                                for s in range(len(boards)):
                                    for f in range(len(boards[s])):
                                        for d in range(len(boards[s][f])):
                                            if boards[s][f][d] != 'fill':
                                                count += boards[s][f][d]

                                return count * bingoNums[i]

                        # Check horizontal
                        hcount = 0
                        for j in range(len(boards)):
                            for s in range(len(boards[j])):
                                for f in range(len(boards[j][s])):
                                    if boards[j][f][s] == 'fill':
                                        hcount += 1
                                if hcount == 5:
                                    count = 0
                                    for ii in range(len(boards)):
                                        for ee in range(len(boards[ii])):
                                            for uu in range(len(boards[ii][ee])):
                                                if boards[ii][ee][uu] != 'fill':
                                                    count += boards[ii][ee][uu]
                                    return count * bingoNums[i]
                                else:
                                    hcount = 0
                                    # jsfd


print(main('input.txt'))
