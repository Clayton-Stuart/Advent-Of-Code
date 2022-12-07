file = open('input.txt', 'r')
ls = file.readlines()
file.close()

for i in range(len(ls)):
    ls[i] = ls[i].strip()

count = 0
chars = []
marker_length = 14

for i in range(len(ls[0])):
    chars.append(ls[0][i])
    count += 1
    if len(chars) > marker_length:
        chars.pop(0)
    if len(chars) == marker_length:
        if (len(chars) > len(set(chars))):
            pass
        else:
            break
        

print(count)