import re

def get_max(array):
    max = 0
    for s in array:
        s = re.split(r'\W+', s)
        if int(s[0]) > max:
            max = int(s[0])
    return max

def main():

    result = 0
    max_red = 12
    max_green = 13
    max_blue = 14
    
    with open("input.txt", "r", encoding='utf8') as file:
        i = 0
        for line in file:
            i = i + 1
            reds = re.findall(r'[0-9]* red', line)
            nb_red = get_max(reds)
            if nb_red > max_red:
                continue
            greens = re.findall(r'[0-9]* green', line)
            nb_green = get_max(greens)
            if nb_green > max_green:
                continue
            blues = re.findall(r'[0-9]* blue', line)
            nb_blue = get_max(blues)
            if nb_blue > max_blue:
                continue
            result = result + i

    print(result)

main()
