import re

def main():
    step_sequence = str()
    mapping = dict()
    with open("input.txt", 'r', encoding="UTF-8") as file:
        for i, line in enumerate(file, start = 1):
            if i == 1:
                step_sequence = re.findall(r'[LR]+', line)[0]
            elif i > 2:
                data = re.findall(r'[A-Z0-9]+', line)
                mapping[data[0]] = [data[1],data[2]]
    start = 'DRA'
    end = 'HMZ'
    actual = start
    steps_taken = 0
    while actual != end:
        if step_sequence[0] == 'L':
            actual = mapping[actual][0]
        elif step_sequence[0] == 'R':
            actual = mapping[actual][1]
        step_sequence = step_sequence[1:] + step_sequence[0]
        steps_taken += 1
    print(steps_taken)

main()
