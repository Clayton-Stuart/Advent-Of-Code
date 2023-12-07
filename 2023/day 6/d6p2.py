file = open('d6-input', 'r')
lines = file.readlines()
file.close()

for i in range(len(lines)):
    lines[i] = int(lines[i].strip().replace(' ', '').split(':')[1])

minimum = 0
maximum = lines[0]

for i in range(lines[0]):
    if i * (lines[0] - i) > lines[1]:
        minimum = i
        break

while True:
    if maximum * (lines[0] - maximum) > lines[1]:
        break
    maximum -= 1

print(maximum - minimum + 1)