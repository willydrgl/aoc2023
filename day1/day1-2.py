digits = {"zero": "0",
          "one": "1",
          "two": "2",
          "three": "3",
          "four": "4",
          "five": "5",
          "six": "6",
          "seven": "7",
          "eight": "8",
          "nine": "9"}

def is_digit(string):
    if string in digits.keys() or string in digits.values():
        return True

def string_to_int(string):
    if string in digits.keys():
        return int(digits[string])
    if string in digits.values():
        return int(string)

def get_line_value(line):
    return str(get_first_digit(line)) + str(get_last_digit(line))

def get_first_digit(line):
    string = ""
    for i in range(0, len(line)-1):
        string = ""
        for j in range(i, len(line)-1):
            string = string + line[j]
            if is_digit(string):
                return string_to_int(string)

def get_last_digit(line):
    string = ""
    for i in range(2, len(line)):
        string = ""
        for j in range(i, len(line)):
            string = line[len(line)-j] + string
            if is_digit(string):
                return string_to_int(string)
    string = line[0]
    return string_to_int(string)

def main():
    answer = 0
    with open("input.txt", "r", encoding='utf8') as file:
        for line in file:
            answer = answer + int(get_line_value(line))
    print(answer)

main()
