import re

def is_stronger(hand, compared_to):
    cards = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10,
             '9': 9, '8': 8, '7': 7, '6': 6,
             '5': 5, '4': 4, '3': 3, '2': 2}
    hand_patterns = []
    compared_to_patterns = []

    for i in range(5, 1, -1):
        for e in cards.keys():
            if hand.count(e) == i:
                hand_patterns.append(i)
            if compared_to.count(e) == i:
                compared_to_patterns.append(i)

    for i, j in zip(hand_patterns, compared_to_patterns):
        if i > j:
            return True
        elif i < j:
            return False
        else:
            continue

    if len(hand_patterns) > len(compared_to_patterns):
        return True
    elif len(hand_patterns) < len(compared_to_patterns):
        return False
    else:
        pass

    for i, j in zip(hand, compared_to):
        if cards[i] > cards[j]:
            return True
        elif cards[i] < cards[j]:
            return False
        else:
            continue

    print("Égalitée ?")


def sort_by_strength(array):
    new_array = []
    for e in array:
        if not new_array:
            new_array.append(e)
        else:
            for i in range(len(new_array)):
                if not is_stronger(e[0], new_array[i][0]):
                    new_array.insert(i, e)
                    break
            if e not in new_array:
                new_array.append(e)
    return new_array

def main():
    with open("input.txt", 'r', encoding="UTF-8") as file:
        data = []
        for line in file:
            data.append(re.findall(r'[AKQJT0-9]+', line))
    data = sort_by_strength(data)

    answer = 0
    for i, e in enumerate(data):
        answer += int(e[1]) * (i+1)
    print(answer)

main()
