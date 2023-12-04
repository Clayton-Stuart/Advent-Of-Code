file = open('d1-input', 'r')
lines = file.readlines()
file.close()

parsed_lines = []

for i in lines:
    parsed_lines.append("")
    for j in i:
        if j in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            parsed_lines[-1] += j

num = 0
for i in parsed_lines:
    if len(i) == 1:
        num += int(i + i)
    else:
        num += int(i[0] + i[-1])

print(num)
