import re

# Techniquement fonctionnel avec heures/journées/mois/années ?
# Pour une vraie solution : faire le PPCM des pas de chaque start

def main():
    step_sequence = str()
    mapping = dict()
    with open("input2.txt", 'r', encoding="UTF-8") as file:
        for i, line in enumerate(file, start = 1):
            if i == 1:
                step_sequence = re.findall(r'[LR]+', line)[0]
            elif i > 2:
                data = re.findall(r'[A-Z0-9]+', line)
                mapping[data[0]] = [data[1],data[2]]
    starts = []
    for e in mapping.keys():
        if e[-1] == 'A':
            starts.append(e)
    actuals = starts.copy()
    steps = []
    looping_steps = []

    for i in range(len(actuals)):
        next_steps = str(step_sequence)

        print(actuals[i], mapping[actuals[i]])
        
        # First time steps
        steps_taken = 0
        while actuals[i][-1] != 'Z':
            if next_steps[0] == 'L':
                actuals[i] = mapping[actuals[i]][0]
            elif next_steps[0] == 'R':
                actuals[i] = mapping[actuals[i]][1]
            next_steps = next_steps[1:] + next_steps[0]
            steps_taken += 1
        steps.append(steps_taken)

        print(actuals[i], mapping[actuals[i]])

        # Second steps
        steps_taken = 0
        if next_steps[0] == 'L':
            actuals[i] = mapping[actuals[i]][0]
        elif next_steps[0] == 'R':
            actuals[i] = mapping[actuals[i]][1]
        next_steps = next_steps[1:] + next_steps[0]
        steps_taken += 1

        next_steps = str(step_sequence)
        while actuals[i][-1] != 'Z':
            if next_steps[0] == 'L':
                actuals[i] = mapping[actuals[i]][0]
            elif next_steps[0] == 'R':
                actuals[i] = mapping[actuals[i]][1]
            next_steps = next_steps[1:] + next_steps[0]
            steps_taken += 1
        looping_steps.append(steps_taken)

        print(actuals[i], mapping[actuals[i]])

    print(steps)
    print(looping_steps)

    i = 1
    actual_steps = steps.copy()
    while True:
        for j in range(len(actual_steps)):
            actual_steps[j] = steps[j] + looping_steps[j] * i
        if len(set(actual_steps)) == 1:
            print(actual_steps[0])
            break
        i = i + 1

main()
