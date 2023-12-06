import re

def process_range(_range, _map):
    for i, n in enumerate(_range):
        for a in _map:
            if a[1] + a[2] > n >= a[1]:
                _range[i] = a[0] + (_range[i] - a[1])
                break
    return _range

"""
# _range: tuple (min, max)
def process_numbers(numbers, maps):
    for m in maps:
        # Adding bottom of ranges to numbers
        for n in numbers:
            for a in m:
                if a[1] not in numbers and a[1] + a[2] > n > a[1]:
                    numbers.append(a[1])
                    break
        # Processing numbers
        for i in range(len(numbers)):
            for a in m:
                if a[1] + a[2] > numbers[i] >= a[1]:
                    numbers[i] = a[0] + (numbers[i] - a[1])
    return min(numbers)
"""

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
        temp.sort(key=lambda x: x[1], reverse=True)
        maps.append(temp)

    # Converting seeds as range tuples
    ranges = []
    for i in range(int(len(seeds)/2)):
        ranges.append([seeds[i*2], seeds[i*2] + seeds[i*2+1]])
    #print("Initial ranges: ", len(ranges))
    # Processing numbers
    for m in maps:
        #print("Map : ", m)
        to_remove = []
        to_add = []
        for t in ranges:
            #print("Range : ", t)
            for a in m:
                if t[0] < a[1] <= a[1] + a[2] < t[1]:
                    to_add.append([t[0], a[1] - 1])
                    to_add.append([a[1] + a[2], t[1]])
                    to_add.append([a[1], a[1] + a[2] - 1])
                    to_remove.append(t)
                    #print("Comparing to range ", a[1], " - ", a[1] + a[2])
                    #print("Spliting a", t, " into ", [t[0], a[1]], " and ", [a[1] + a[2], t[1]])
                    break
                elif t[0] < a[1] < t[1]:
                    to_add.append([t[0], a[1]])
                    to_add.append([a[1] - 1, t[1]])
                    to_remove.append(t)
                    #print("Comparing to range ", a[1], " - ", a[1] + a[2])
                    #print("Spliting b", t, " into ", [t[0], a[1]], " and ", [a[1], t[1]])
                    break
                elif t[0] < a[1] + a[2] < t[1]:
                    to_add.append([t[0], a[1] + a[2]])
                    to_add.append([a[1] + a[2] - 1, t[1]])
                    to_remove.append(t)
                    #print("Comparing to range ", a[1], " - ", a[1] + a[2])
                    #print("Spliting c", t, " into ", [t[0], a[1] + a[2]], " and ", [a[1] + a[2], t[1]])
                    break

        #print("Need to remove : ", len(to_remove))
        for t in to_remove:
            ranges.remove(t)
        #print("Ranges left : ", len(ranges))

        #print("Need to add : ", len(to_add))
        for t in to_add:
            ranges.append(t)
        #print("Ranges left : ", len(ranges))

        #print("Converting...")
        for i in range(len(ranges)):
            #print("Converting ", ranges[i], "...")
            ranges[i] = process_range(ranges[i], m)
            #print("... into ", ranges[i])


    locations = []
    for p in ranges:
        locations.append(p[0])
        print(p[0])
    print(min(locations))



    
    """
    numbers2 = []
    for pair in numbers:
        numbers2.append(pair[0])
        numbers2.append(pair[1])
    # Pass seeds through the maps to get the locations
    for array in maps:
        numbers2 = process_numbers(numbers2, array)
    print(min(numbers2))
    """
    """
        # Processing numbers
        for i in range(len(numbers)):
            for a in m:
                if a[1] + a[2] > numbers[i] >= a[1]:
                    numbers[i] = a[0] + (numbers[i] - a[1])
    return min(numbers)
    """


    """
            if lowest_location == -1:
                lowest_location = number
            else:
                lowest_location = min(lowest_location, number)"""
    """
    Brute forcing uwu
    
    lowest_location = -1
    for i in range(int(len(seeds)/2)):
        print("Groupe de seeds ", i, "/10")
        for j in range(seeds[i*2+1]):
            number = seeds[i*2]+j
            for array in maps:
                number = process_number(number, array)
            if lowest_location == -1:
                lowest_location = number
            else:
                lowest_location = min(lowest_location, number)
    """

main()
