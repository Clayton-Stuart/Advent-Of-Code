def main(file):
    bins = open(file)
    ls = bins.readlines()
    bins.close()
    fin_gam = ''
    fin_eps = ''
    for i in range(len(ls[0]) - 1):
        ones = 0
        zeros = 0
        for e in range(len(ls)):
            if ls[e][i] == '0':
                zeros += 1
            elif ls[e][i] == '1':
                ones += 1 
        if ones > zeros:
            fin_gam += '1'
            fin_eps += '0'

        elif zeros > ones:
            fin_gam += '0'
            fin_eps += '1'
    return (fin_gam, fin_eps)

print(main("example.txt"))

