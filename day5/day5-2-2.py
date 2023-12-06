import re

maps = []
seeds = []
ranges = []
to_remove = []
locations = []

def split_range(_range, _map):
    for array in m:
        
        destination_start = a[0]
        source_start = a[1]
        source_end = a[1] + a[2]
        
        if _range[0] < source_start < source_end < _range[1]:
            ranges.insert([_range[0], source_start - 1])
            ranges.insert([source_start + source_range, _range[1]])
            ranges.insert([source_start, source_end - 1])
            to_remove.append(_range)

        elif _range[0] < source_start < _range[1]:
            ranges.insert([_range[0], source_start])
            ranges.insert([source_start - 1, _range[1]])
            to_remove.append(_range)


        # SOURCE END -1 première array ???
        elif _range[0] < source_end < _range[1]:
            ranges.insert([_range[0], source_end])
            ranges.insert([source_end - 1, _range[1]])
            to_remove.append(_range)

def main():

    # Converting file to usable format
    with open("input.txt", "r", encoding='utf8') as file:
        data = file.read().replace('\n', ' ')
    data = re.split('  ', data)

    for i, array in enumerate(data):
        data[i] = re.split(':', data[i])
        data[i][1] = re.findall(r'[0-9]+', data[i][1])

    # Registering seeds and maps
    seeds = data[0][1]
    for i in range(len(seeds)):
        seeds[i] = int(seeds[i])
    data.pop(0)

    for array in data:
        temp = []
        for i in range(int(len(array[1])/3)):
            temp.append(array[1][i*3:i*3+3])
            for j in range(len(temp[i])):
                temp[i][j] = int(temp[i][j])
        temp.sort(key=lambda x: x[1], reverse=True)
        maps.append(temp)

    # Converting seeds as range arrays
    for i in range(int(len(seeds)/2)):
        ranges.append([seeds[i*2], seeds[i*2] + seeds[i*2+1]])

    # Processing numbers
    for m in maps:
        to_remove = []
        for e in ranges:
            split_range(e, m)
        for e in to_remove:
            ranges.remove(e)

    # Register locations and print the smallest
    for e in ranges:
        locations.append(e[0])
    print(min(locations))

main()
