import re

maps = []
seeds = []
ranges = []
locations = []

def split_range(_index, _range, _map):
    for array in _map:
        destination_start = array[0]
        source_start = array[1]
        source_end = array[1] + array[2]
        
        if _range[0] < source_start < source_end < _range[1]:
            ranges[_index] = [_range[0], source_start - 1]
            ranges.insert(_index + 1, [source_start, source_end])
            ranges.insert(_index + 2, [source_end + 1, _range[1]])
            break

        elif _range[0] < source_start < _range[1]:
            ranges[_index] = [_range[0], source_start -1 ]
            ranges.insert(_index + 1, [source_start, _range[1]])
            break

        elif _range[0] < source_end < _range[1]:
            ranges[_index] = [_range[0], source_end -1 ]
            ranges.insert(_index + 1, [source_end, _range[1]])
            break
        
def process_range(_range, _map):
    for i, n in enumerate(_range):
        for a in _map:
            if a[1] + a[2] > n >= a[1]:
                _range[i] = a[0] + (_range[i] - a[1])
                break
    return _range

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
        temp.sort(key=lambda x: x[1])
        maps.append(temp)

    # Converting seeds as range arrays
    for i in range(int(len(seeds)/2)):
        ranges.append([seeds[i*2], seeds[i*2] + seeds[i*2+1]])

    # Processing numbers
    for m in maps:
        for i, e in enumerate(ranges):
            split_range(i, e, m)
        for e in ranges:
            process_range(e, m)

    # Register locations and print the smallest
    for e in ranges:
        locations.append(e[0])
        
    print(min(locations))

main()
