import re

answer = 0

def calculate_possibilities(row, sizes, i):
    global answer
    if i < len(row):
        if row[i] == '?':
            i = i + 1
            calculate_possibilities(row[:i-1]+'#'+row[i:], sizes, i)
            calculate_possibilities(row[:i-1]+'.'+row[i:], sizes, i)
        else:
            calculate_possibilities(row, sizes, i+1)
    else:
        groups = re.findall(r'[#]+', row)
        if len(groups) != len(sizes):
            return 1
        for g, s in zip(groups, sizes):
            if len(g) != int(s):
                return 1
        answer += 1
        return 0
    return 1

def main():
    data = []

    with open("input.txt", 'r', encoding="UTF-8") as file:
        for line in file:
            data.append(re.split(' ', line[:-1]))

        # :clown:
        for e in data:
            e[0] = ((e[0]+'?')*5)[:-1]
            e[1] = ((e[1]+',')*5)[:-1]

    for i, e in enumerate(data):
        row = e[0]
        sizes = re.findall(r'[0-9]+', e[1])
        calculate_possibilities(row, sizes, 0)

    print(answer)

main()
