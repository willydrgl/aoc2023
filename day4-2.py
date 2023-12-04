import re

original_cards = []
scratchcards = {}

def process_card(i, card):
    # Count number of winning numbers
    nb_winning_numbers = 0
    for number in card[1]:
        if is_winning_number(number, card[0]):
            nb_winning_numbers += 1
    # Add cards to scratchcards total
    for j in range(1, nb_winning_numbers + 1):
        if i + j < len(original_cards):
            if not scratchcards[i+j]:
                scratchcards[i+j] = 1
            else:
                scratchcards[i+j] += 1
        else:
            break

def is_winning_number(number, winning_numbers):
    for n in winning_numbers:
        if number == n:
            return True
    return False

def main():
    # """""" EXAMPLE
    with open("example.txt", "r", encoding='utf8') as file:
        for line in file:
            winning_numbers = []
            selected_numbers = []
            split_card = re.split(r'\s+', line)[2:]
            for number in split_card[:split_card.index('|')]:
                winning_numbers.append(number)
            for number in split_card[split_card.index('|')+1:-1]:
                selected_numbers.append(number)
            card = (winning_numbers, selected_numbers)
            original_cards.append(card)
    for i, card in enumerate(original_cards):
        # Put original copy in scratchcards
        if not scratchcards[i]:
            scratchcards[i] = 1
        else:
            scratchcards[i] += 1
        for j in range(scratchcards[i].value()):
            process_card(i, card)
    print(scratchcards)

main()
