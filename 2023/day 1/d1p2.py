file = open('d1-input', 'r')
lines = file.readlines()
file.close()

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
word_to_digit = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

parsed_lines = []

for i in lines:
    keys = list(word_to_digit.keys())
    parsed_lines.append("")
    cur_indexes = {}

    for e in keys:
        if i.find(e)!= -1:
            cur_indexes[i.find(e)] = e

    indexes = list(cur_indexes.keys())
    indexes.sort()


    for e in indexes:
        i = i.replace(cur_indexes[e], word_to_digit[cur_indexes[e]])

    for j in i:
        if j in digits:
            parsed_lines[-1] += j





num = 0
for i in parsed_lines:
    if len(i) == 1:
        num += int(i + i)
    else:
        num += int(i[0] + i[-1])

print(num)
