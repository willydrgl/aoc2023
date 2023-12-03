import re

# Lists of tuples (Match_object, line_in_file)
numbers = []
stars = []

def gear_power(star):
    adjacent_numbers = []
    for n in numbers:
        if star[1] - 1 <= n[1] <= star[1] + 1:
            for i in range(n[0].start(), n[0].end()):
                if star[0].start() - 1 <= i <= star[0].start() + 1:
                    adjacent_numbers.append(int(n[0].group(0)))
                    break
    if len(adjacent_numbers) == 2:
        return adjacent_numbers[0] * adjacent_numbers[1]
    return 0

def main():
    answer = 0
    with open("input.txt") as file:
        for i, line in enumerate(file, start=1):
            matches = re.finditer(r'[0-9]+', line)
            for m in matches:
                numbers.append((m, i))
            matches = re.finditer(r'\*', line)
            for m in matches:
                stars.append((m, i))
    for s in stars:
        answer = answer + gear_power(s)
    print(answer)

main()
