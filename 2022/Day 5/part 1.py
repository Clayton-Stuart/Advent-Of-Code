file = open('input.txt', 'r')
ls = file.readlines()
file.close()

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

break_index = 0
for i in range(len(ls)):
    if ls[i] == '\n':
        break_index = i
        break

for i in range(len(ls)):
    ls[i] = ls[i].strip('\n')

nums = ls[break_index - 1].split(' ')

while nums.count('') > 0:
    nums.remove('')

for i in range(len(nums)):
    nums[i] = int(nums[i])

nums.sort(reverse=True)
lines = []

for _ in range(nums[0]):
    lines.append([])

del ls[break_index - 1]

count = 0
while ls[count] != '':
    ls[count] = ls[count].replace('    ', '-')
    ls[count] = ls[count].replace(' ', '')
    ls[count] = ls[count].replace('[', '')
    ls[count] = ls[count].replace(']', '')

    count += 1

count = 0
while ls[count]!= '':
    for i in range(len(ls[count])):
        if ls[count][i]!= '-':
            lines[i].append(ls[count][i])

    count += 1

while ls[0] != '':
    del ls[0]
del ls[0]

for i in range(len(ls)):
    ls[i] = ls[i].split(' ')



for i in range(len(ls)):
    ls[i].remove('move')
    ls[i].remove('from')
    ls[i].remove('to')

for i in range(len(ls)):
    for e in range(len(ls[i])):
        ls[i][e] = int(ls[i][e])


# All of the parsing is above. Anything below this comment is to execute the instructions in the input 


for i in range(len(ls)):
    for _ in range(ls[i][0]):
        lines[ls[i][2] - 1].insert(0, lines[ls[i][1] - 1].pop(0))
final = ''
for i in lines:
    final += i[0]
print(final)

