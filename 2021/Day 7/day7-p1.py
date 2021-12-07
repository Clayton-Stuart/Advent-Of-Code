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
    median = statistics.median(ls)

    fuel = 0
    # Get fuel amounts
    for i in range(len(ls)):
        if ls[i] < median:
            fuel += median - ls[i]
        elif ls[i] > median:
            fuel += ls[i] - median
        elif ls[i] == median:
            fuel += 0

    return fuel

print(main('input.txt'))