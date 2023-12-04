import re

def is_winning_number(number, winning_numbers):
    for n in winning_numbers:
        if number == n:
            return True
    return False

def main():
    total_points = 0
    with open("input.txt", "r", encoding='utf8') as file:
        for line in file:
            card_points = 0
            winning_numbers = []
            card = re.split(r'\s+', line)[2:]
            for n in card[:card.index('|')]:
                winning_numbers.append(n)
            for n in card[card.index('|')+1:-1]:
                if is_winning_number(n, winning_numbers):
                    if card_points > 0:
                        card_points = card_points * 2
                    else:
                        card_points = 1
            total_points = total_points + card_points
    print(total_points)

main()
