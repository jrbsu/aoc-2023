with open("data.txt", "r") as f:
    data = f.read()
all_lines = data.split('\n')

all_readings = []
for x in all_lines:
    all_readings.append(x.split(" "))

def find_difference(reading):
    new_reading = []
    for count, number in enumerate(reading):
        if count == 0:
            continue
        else:
            difference = int(number) - int(reading[count-1])
        new_reading.append(difference)
    return new_reading

def check_if_zero(reading):
    a = True
    for x in reading:
        if x != 0:
            a = False
    return a

def make_int(reading):
    new_reading = []
    for x in reading:
        x = int(x)
        new_reading.append(x)
    return new_reading

def add_numbers(sequences):
    total_sequences = len(sequences)
    zeros = sequences[-1]
    zeros.append(0)
    for x in range(total_sequences):
        a = (1 + x) * -1
        if a == -1: # If this is the last sequence, it's the zeros and we don't need to modify it again
            continue
        else: # This isn't the zeroes so we can use the previous value to find out the next one
            b = a + 1
            new_number = sequences[b][-1] + sequences[a][-1]
            sequences[a].append(new_number)
    return sequences[0][-1]

result = 0

for x in all_readings:
    x = make_int(x)
    sequences = []
    new_sequence = x
    sequences.append(new_sequence)
    while check_if_zero(new_sequence) == False:
        new_sequence = find_difference(new_sequence)
        sequences.append(new_sequence)
    result += add_numbers(sequences)

print(result)