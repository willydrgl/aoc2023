digits = ["0","1","2","3","4","5","6","7","8","9"]

def get_line_value(line):
    return get_first_digit(line) + get_last_digit(line)

def get_first_digit(line):
    for c in line:
        if c in digits:
            return c

def get_last_digit(line):
    for c in line[::-1]:
        if c in digits:
            return c

def main():
    answer = 0
    with open("input.txt", "r", encoding='utf8') as file:
        for line in file:
            answer = answer + int(get_line_value(line))
    print(answer)

main()
