file = open('input.txt', 'r')
ls = file.readlines()
file.close()

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
current_path = []
used_names = []
current_directory = '/'
limit = 100000
directories = {'/': 0}


# Strip new line characters
for i in range(len(ls)):
    ls[i] = ls[i].strip()

for i in ls:
    if i.split(' ')[0] == 'dir':
        directories[i.split(' ')[1]] = 0



for i in range(len(ls)):
    command = ls[i].split(' ')

    # check if the line is a command
    if command[0] == '$':
        if command[1] == 'cd':
            if command[2] == '..':
                current_path.pop()


            elif command[2] not in used_names:
                used_names.append(command[2])
                current_path.append(command[2])
            else:
                used_names.append(command[2] + str(i))
                current_path.append(command[2] + str(i))
                directories[command[2] + str(i)] = 0

    # The line is an output
    else:
        if ls[i][0] in digits:
            for e in current_path:
                directories[e] += int(command[0])
            
final = 0
for key in directories:
    if directories[key] <= limit:
        final += directories[key]

print(final)
