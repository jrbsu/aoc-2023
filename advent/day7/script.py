import re
import collections
import pandas as pd

with open("data.txt", "r") as f:
    data = f.read()
hands = data.split('\n')

score_dict = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}

five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pair = []
one_pair = []
no_pair = []

all_lists = [five_of_a_kind, four_of_a_kind, full_house, three_of_a_kind, two_pair, one_pair, no_pair]

def make_cards(hand):
    return list(re.search(r".{5}", hand).group())

def count_cards(cards):
    counter = dict(collections.Counter(cards))
    return counter

def sort_hand(card_values):
    if len(card_values.keys()) == 1:
        five_of_a_kind.append(hand)
    elif len(card_values.keys()) == 2:
        if 4 in list(card_values.values()):
            four_of_a_kind.append(hand)
        else:
            full_house.append(hand)
    elif len(card_values.keys()) == 5:
        no_pair.append(hand)
    elif len(card_values.keys()) == 3:
        if 3 in list(card_values.values()):
            three_of_a_kind.append(hand)
        else:
            two_pair.append(hand)
    else:
        one_pair.append(hand)

def give_scores(hand):
    cards = make_cards(hand)
    new_hand = []
    for x in cards:
        new_hand.append(int(score_dict.get(str(x))))
    return(new_hand)

def make_dataframe(array):
    df_data = []
    for hand in array:
        cards = give_scores(hand)
        bid = re.search("(\d+)$", hand).group()
        cards.append(bid)
        cards.append(hand)
        df_data.append(cards)
    df = pd.DataFrame(df_data, columns=['card1', 'card2', 'card3', 'card4', 'card5', 'bid', 'hand'])
    df = df.sort_values(['card1', 'card2', 'card3', 'card4', 'card5'], ascending=[False, False, False, False, False])
    return df

for hand in hands:
    cards = make_cards(hand)
    card_values = count_cards(cards)
    sort_hand(card_values)

dataframes = []

for x in all_lists:
    dataframes.append(make_dataframe(x))

out = pd.concat(dataframes).values.tolist()

winnings = 0

for c, x in enumerate(out):
    rank = 1000 - c
    score = rank * int(x[5])
    winnings += score

print(winnings)