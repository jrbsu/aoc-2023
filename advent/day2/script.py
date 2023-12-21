import re

with open("data.txt", "r") as f:
    data = f.read()

data = data.split("\n")

totals = {}
game_log = []

for count, game in enumerate(data):
    count = count + 1

    red_total = re.findall(r'(\d+)\sred', game)
    red_max = 0
    for x in red_total:
        y = int(x)
        if y > red_max:
            red_max = y

    green_total = re.findall(r'(\d+)\sgreen', game)
    green_max = 0
    for x in green_total:
        y = int(x)
        if y > green_max:
            green_max = y

    blue_total = re.findall(r'(\d+)\sblue', game)
    blue_max = 0
    for x in blue_total:
        y = int(x)
        if y > blue_max:
            blue_max = y
        
    totals[count] = [red_max, green_max, blue_max]

    if (red_max <= 12 and green_max <= 13 and blue_max <= 14):
        game_log.append(count)

powers = 0

for x in totals.values():
    powers += (x[0] * x[1] * x[2])

print(powers)