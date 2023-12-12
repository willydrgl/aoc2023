import re

def predict_next_value(sequence):
    i = 0
    steps = []
    while i < len(sequence) - 1:
        steps.append(str(int(sequence[i+1]) - int(sequence[i])))
        i = i + 1
    if len(set(steps)) == 1 and steps[0] == '0':
        return sequence[i]
    next_value = str(int(sequence[i]) + int(predict_next_value(steps)))
    return next_value

def main():
    data = []
    with open("input.txt", 'r', encoding="UTF-8") as file:
        for line in file:
            data.append(re.findall(r'[\+\-0-9]+', line))
    answer = 0
    for e in data:
        answer += int(predict_next_value(e))
    print(answer)

main()
