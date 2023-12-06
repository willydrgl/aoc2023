import re

def nb_valid_options(time, distance):
    answer = 0
    speed = 0
    for i in range(1, time):
        speed = i
        remaining_time = time - i
        if speed * remaining_time > distance:
            answer += 1
    return answer

def main():
    table = []
    with open("input.txt", "r", encoding='utf8') as file:
        i = 0
        for line in file:
            array = re.findall(r'[0-9]+', line)
            string = ''
            for e in array:
                string += e
            table.append(int(string))
            i = i + 1

    time = table[0]
    distance = table[1]
    answer = nb_valid_options(time, distance)
    print(answer)

main()
