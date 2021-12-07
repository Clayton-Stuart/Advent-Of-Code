import statistics

def main(file):
    # Get data from file
    doc = open(file, 'r')
    ls = doc.readline()
    doc.close()
    ls = ls.split(',')
    for i in range(len(ls)):
        ls[i] = int(ls[i])
     
    # Get median from data set
    mean = statistics.mean(ls)
    print(mean)
    mean = int(round(mean))
    print(mean)
    mean = 489

    fuel = 0
    # Get fuel amounts
    for i in range(len(ls)):
        if ls[i] < mean:
            for e in range(mean - ls[i]):
                fuel += e + 1
        elif ls[i] > mean:
            for e in range(ls[i] - mean):
                fuel += e + 1
        elif ls[i] == mean:
            fuel += 0

    return fuel

print(main('input.txt'))