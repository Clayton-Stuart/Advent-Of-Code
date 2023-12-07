from tqdm import tqdm

file = open('d5-input', 'r')
lines = file.readlines()
file.close()

def get_seed_path(seed_num):
    processed = False
    for i in sections:
        for j in i:
            if isinstance(j[0], int):
                destination_range = j[0]
                source_range = j[1]
                range_length = j[2]
                if seed_num < source_range + range_length and seed_num >= source_range and not processed:
                    seed_num = destination_range + seed_num - source_range
                    processed = True
            else:
                processed = False

    return seed_num


seeds = list(map(int, lines[0].strip().split(': ')[1].split(' ')))

del lines[0]

sections = []

for i in range(len(lines)):
    if lines[i] == '\n':
        sections.append([])
    elif lines[i][0] not in '0123456789':
        sections[-1].append(lines[i].split(":")[0])
    else:
        sections[-1].append(list(map(int, lines[i].strip().split(" "))))


seed_locations = get_seed_path(seeds[0])

pairs = []

for i in range(len(seeds)):
    if i % 2 == 0:
        pairs.append([seeds[i], seeds[i + 1]])

length = len(pairs)
for i in range(len(pairs)):
    print(i, '/', length)
    for e in tqdm(range(pairs[i][1])):
        cur_seed_location = get_seed_path(pairs[i][0] + e)
        if cur_seed_location < seed_locations:
            seed_locations = cur_seed_location

print(seed_locations)
