import re

schematics = []
numbers = []

def has_adjacent_char(match, line):
    for i in range(match.start(), match.end()):
        for x in range(-1, 2):
            for y in range(-1, 2):
                try:
                    if re.match(r'[^0-9.\n]', schematics[line+x][i+y]):
                        return True
                except:
                    pass
    return False


def main():
    answer = 0
    with open("input.txt") as file:
        for i, line in enumerate(file, start=1):
            # Convert input to array
            schematics.append([])
            for char in line:
                schematics[i-1].append(char)
            # Register numbers and their lines in an array
            matches = re.finditer(r'[0-9]+', line)
            for m in matches:
                numbers.append((m, i-1))
    for n in numbers:
        if has_adjacent_char(n[0], n[1]):
            answer = answer + int(n[0].group(0))
    print(answer)

main()
