import re

def main():
    data = []
    with open("input.txt", 'r', encoding="UTF-8") as file:
        for line in file:
            if not data:
                for i in range(len(line)):
                    data.append('')
            for i, c in enumerate(line[:-1]):
                data[i] = data[i] + c

    processed_data = []
    for i in range(len(data)):
        split = re.split(r'(#)', data[i])
        new_line = ''
        for s in split:
            if s == '#':
                new_line += s
            else:
                new_line += 'O' * s.count('O') + '.' * s.count('.')
        processed_data.append(new_line)

    answer = 0
    for line in processed_data:
        for i, char in enumerate(line):
            if char == 'O':
                answer += len(line) - i

    print(answer)

main()
