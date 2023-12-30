import re

def find_mirror(pattern):
    for i in range(len(pattern)-1):
        if pattern[i] == pattern[i+1]:
            b = False
            for j in range(1, len(pattern[i:])-1):
                if i-j < 0:
                    break
                if pattern[i-j] != pattern[i+1+j]:
                    b = True
                    break
                else:
                    continue
            if not b:
                return i+1
    return 0

def main():
    data = []
    with open("input.txt", 'r', encoding="UTF-8") as file:
        pattern = []
        for line in file:
            if not re.match(r'[#.]+', line):
                data.append(pattern)
                pattern = []
            else:
                pattern.append(re.findall(r'[\#\.]+', line)[0])

    total_left = 0
    total_up = 0

    for pattern in data:
        # search for horizontal mirror
        total_up += find_mirror(pattern)
        # search for vertical mirror
        flip_pattern = []
        for i in range(len(pattern[0])):
            flip_pattern.append('')
            for e in pattern:
                flip_pattern[i] += e[i]
        total_left += find_mirror(flip_pattern)
        # printing
        """
        print("-----")
        print("Pattern :")
        for e in pattern:
            print(e)
        print("Up : ", find_mirror(pattern))
        print("Flipped :")
        for e in flip_pattern:
            print(e)
        print("Left :", find_mirror(flip_pattern))
        """

    print(total_left + 100 * total_up)

main()
