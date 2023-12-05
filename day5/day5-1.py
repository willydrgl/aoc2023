import re

def process_seeds(seeds, mapp):
    print(mapp)

def main():

    # Converting file to usable format
    with open("example.txt", "r", encoding='utf8') as file:
        data = file.read().replace('\n', ' ')
    data = re.split('  ', data)

    for i, array in enumerate(data):
        data[i] = re.split(':', data[i])
        data[i][1] = re.findall(r'[0-9]+', data[i][1])

    # Registering seeds and maps
    seeds = data[0][1]
    data.pop(0)

    maps = []
    for array in data:
        temp = []
        for i in range(int(len(array[1])/3)):
            temp.append(array[1][i*3:i*3+3])
        temp.sort(key=lambda x: x[0], reverse=True)
        maps.append(temp)

    # Pass seeds through the maps
    for array in maps:
        process_seeds(seeds, array)

main()
