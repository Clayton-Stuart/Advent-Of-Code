file = open('d3-input', 'r')
lines = file.readlines()
file.close()

characters = []
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

in_number = False

for line in lines:
    for e in line.strip():
        if e not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'] and e not in characters:
            characters.append(e)

for i in range(len(lines)):
    lines[i] = lines[i].strip()

new_array = []
nums = []

for line in lines:
    new_array.append([])
    for i in line:
        if i not in digits:
            new_array[-1].append(i)
            in_number = False
        else:
            if in_number == False:
                in_number = True
                nums.append('')
                nums[-1] += i
            elif in_number == True:
                in_number = True
                nums[-1] += i
            new_array[-1].append(len(nums) - 1)

num = 0
counted = []



for i in range(len(new_array)):
    for j in range(len(new_array[i])):
        if new_array[i][j] == '*':
            touching_vals = []
            touching_vals_sorted = []
            if i > 0:
                if isinstance(new_array[i - 1][j], int):    
                    touching_vals.append(new_array[i - 1][j])
                if j > 0:
                    if isinstance(new_array[i - 1][j - 1], int):        
                        touching_vals.append(new_array[i - 1][j - 1])
                if j < len(new_array[i]) - 1:
                    if isinstance(new_array[i - 1][j + 1], int):        
                        touching_vals.append(new_array[i - 1][j + 1])

            if i < len(new_array) - 1:
                if isinstance(new_array[i + 1][j], int):    
                    touching_vals.append(new_array[i + 1][j])
                if j > 0:
                    if isinstance(new_array[i + 1][j - 1], int):        
                        touching_vals.append(new_array[i + 1][j - 1])
                if j < len(new_array[i]) - 1:
                    if isinstance(new_array[i + 1][j + 1], int):        
                        touching_vals.append(new_array[i + 1][j + 1])

            if j > 0:
                if isinstance(new_array[i][j - 1], int):    
                    touching_vals.append(new_array[i][j - 1])
            if j < len(new_array[i]) - 1:
                if isinstance(new_array[i][j + 1], int):    
                    touching_vals.append(new_array[i][j + 1])

            for e in touching_vals:
                if e not in touching_vals_sorted:
                    touching_vals_sorted.append(e)

            if len(touching_vals_sorted) == 2:
                counted.append([int(nums[touching_vals_sorted[0]]), int(nums[touching_vals_sorted[1]])])


for i in counted:
    num += i[0] * i[1]

print(num)
