import re

with open("data.txt", "r") as f:
    data = f.read()
nodes = data.split('\n')

path = nodes[0] * 1000
nodes = nodes[2:]

dict_left = {}
dict_right = {}
locations = []
for node in nodes:
    locations.append(re.findall(r'\w{3}', node))

for x in locations:
    dict_left[x[0]] = x[1]
    dict_right[x[0]] = x[2]

directions = list(path)
current_node = "AAA"
steps = 0

for direction in directions:
    if direction == "L":
        print("Turning left...")
        current_node = dict_left[current_node]
    elif direction == "R":
        print("Turning right...")
        current_node = dict_right[current_node]
    steps += 1
    print(f"Now at {current_node}")
    if current_node == "ZZZ":
        print(steps, "steps")
        break