import re

def process_numbers(_numbers, _map):
    new_numbers = _numbers
    for i, n in enumerate(_numbers):
        for a in _map:
            if a[1] + a[2] > n >= a[1]:
                new_numbers[i] = a[0] + (n - a[1])
                break
    return new_numbers

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

    maps = []
    for array in data:
        temp = []
        for i in range(int(len(array[1])/3)):
            temp.append(array[1][i*3:i*3+3])
            for j in range(len(temp[i])):
                temp[i][j] = int(temp[i][j])
        temp.sort(key=lambda x: x[0], reverse=True)
        maps.append(temp)

    # Pass seeds through the maps to get the locations
    numbers = seeds
    for array in maps:
        numbers = process_numbers(numbers, array)
    print(min(numbers))

main()
