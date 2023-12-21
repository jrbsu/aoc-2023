import re

with open("data.txt", "r") as f:
    data = f.read()

times = data.split('\n')[0]
distances = data.split('\n')[1]
times = re.findall(r'(\d+)', times)
distances = re.findall(r'(\d+)', distances)
times = ''.join(times)
distances = ''.join(distances)

winning_combos = 0
for x in range(int(times)):
    speed = x
    release_time = int(times) - x
    
    distance = speed * release_time
    if distance > int(distances):
        winning_combos += 1

print(winning_combos)