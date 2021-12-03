def main(file):
    bins = open(file)
    ox = bins.readlines()
    bins.close()
    bins = open(file)
    co2 = bins.readlines()
    bins.close()

    ox_bin = '' 
    

    # Oxygen
    # Choose by most common bit in column
    for i in range(len(ox[0]) - 1):
        zeros = 0
        ones = 0
        sort = ''
        to_del = []

        # Find most common bit in given column
        for e in range(len(ox)):
            if ox[e][i] == '0':
                zeros += 1
            elif ox[e][i] == '1':
                ones += 1
        if zeros > ones:
            sort = '0'
        elif ones > zeros:
            sort = '1'
        elif ones == zeros:
            sort = '1'

        # Get values to delete
        for e in range(len(ox)):
            if ox[e][i] != sort:
                to_del.append(e)
        
        # reverse deletion list
        mid = []
        for e in range(len(to_del)):
            mid.append(to_del[(e + 1) * -1])
        to_del = mid

        
        # Delete values
        for e in range(len(to_del)):
            ox.pop(to_del[e])

        if len(ox) == 1:
            break


    # C02
    # Choose by most least bit in column
    for i in range(len(co2[0]) - 1):
        zeros = 0
        ones = 0
        sort = ''
        to_del = []

        # Find most least bit in given column
        for e in range(len(co2)):
            if co2[e][i] == '0':
                zeros += 1
            elif co2 [e][i] == '1':
                ones += 1
        
        # Decrypt least common value
        if zeros < ones:
            sort = '0'
        elif ones < zeros:
            sort = '1'
        elif ones == zeros:
            sort = '0'

        # Get indexes of unmatched values
        for e in range(len(co2)):
            if co2[e][i] != sort:
                to_del.append(e)

        # reverse deletion list
        mid = []
        for e in range(len(to_del)):
            mid.append(to_del[(e + 1) * -1])
        to_del = mid


        # delete original values
        for e in range(len(to_del)):
            co2.pop(to_del[e])

        if len(co2) == 1:
            break

    return (ox, co2)

print(main("input.txt"))