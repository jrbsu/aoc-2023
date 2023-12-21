import re
import time

with open("data.txt", "r") as f:
    data = f.read()
cards = data.split('\n')

all_cards = []

for count, card in enumerate(cards):
    winning_numbers = re.search(r':\s(.*?)\s\|', card).group()
    winning_numbers = re.findall(r'\d+', winning_numbers)
    my_numbers = re.search(r'\|.*?$', card).group()
    my_numbers = re.findall(r'\d+', my_numbers)

    card_data = [count, winning_numbers, my_numbers]
    all_cards.append(card_data)

for count, card in enumerate(all_cards):
    print("working on card", card[0])
    time.sleep(1)
    card_hits = 0
    for number in card[2]:
        if number in card[1]:
            card_hits += 1
    print("there were", card_hits, "hits")
    time.sleep(1)
    min_offset = card[0] + 1
    max_offset = card[0] + card_hits
    for card in all_cards:
        print("card[0] is", card[0])
        if card[0] > min_offset and card[0] < max_offset:
            all_cards.append(card)
            print("added card", card[0])

print(len(all_cards))