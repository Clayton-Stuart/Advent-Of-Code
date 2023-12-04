file = open('test', 'r')
lines = file.readlines()
file.close()



digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
word_to_digit = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9'
}



parsed_lines = []

def find_all_indexes(string, item):
    indexes = []
    replace = ""
    for _ in range(len(item)):
        replace += '-'
    while item in string:
        indexes.append(string.find(item))
        string = string.replace(item, replace, 1)
    return indexes

for i in lines:
    keys = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    parsed_lines.append("")
    cur_indexes = {}
    
    for e in keys:
        indexes = find_all_indexes(i, e)
        if len(indexes) > 0:
            for j in indexes:
                cur_indexes[j] = e

    indexes = list(cur_indexes.keys())
    indexes.sort()

    for e in indexes:
        parsed_lines[-1] += word_to_digit[cur_indexes[e]]





num = 0
for i in parsed_lines:
    if len(i) == 1:
        num += int(i + i)
    else:
        num += int(i[0] + i[-1])

print(num)
