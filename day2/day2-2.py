import re

def get_max(array):
    max = 0
    for s in array:
        s = re.split(r'\W+', s)
        if int(s[0]) > max:
            max = int(s[0])
    return max

def main():

    power = 0
    
    with open("input.txt", "r", encoding='utf8') as file:
        for line in file:
            reds = re.findall(r'[0-9]* red', line)
            nb_red = get_max(reds)
            greens = re.findall(r'[0-9]* green', line)
            nb_green = get_max(greens)
            blues = re.findall(r'[0-9]* blue', line)
            nb_blue = get_max(blues)
            game_power = nb_red * nb_green * nb_blue
            power = power + game_power
    print(power)

main()
