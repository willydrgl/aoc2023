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
            table.append([])
            for e in re.findall(r'[0-9]+', line):
                table[i].append(int(e))
            i = i + 1

    times = table[0]
    distances = table[1]
    answer = 1
    for t, d in zip(times, distances):
        answer *= nb_valid_options(t, d)

    print(answer)

main()
