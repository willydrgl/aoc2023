import re

def calculate_possibilities(row, sizes, i, p = 0):
    print(i)
    if i < len(row):
        if row[i] == '?':
            i = i + 1
            p += calculate_possibilities(row[:i-1]+'#'+row[i:], sizes, i, p)
            p += calculate_possibilities(row[:i-1]+'.'+row[i:], sizes, i, p)
        else:
            p += calculate_possibilities(row, sizes, i+1, p)
    else:
        groups = re.findall(r'[#]+', row)
        print(groups)
        if len(groups) != len(sizes):
            print("a")
            return 0
        for g, s in zip(groups, sizes):
            print("b")
            if len(g) != s:
                return 0
        print("c")
        return 1
    return p

def main():
    data = []
    with open("example.txt", 'r', encoding="UTF-8") as file:
        for line in file:
            data.append(re.split(' ', line[:-1]))
    answer = 0
    for e in data:
        row = e[0]
        sizes = re.split(',', e[1])
        answer += calculate_possibilities(row, sizes, 0)
        break
    print(answer)

main()
