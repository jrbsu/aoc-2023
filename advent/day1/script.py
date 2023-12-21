import re

raw_data = open("data.txt", "r")
data = [line.strip() for line in raw_data]

total = 0

numbers_list = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
regex = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'

def get_digit(x):
    return x if x.isnumeric() else str(numbers_list.index(x))

for word in data:
    digits = re.findall(regex, word)
    value = int(get_digit(digits[0]) + get_digit(digits[-1]))
    total += value

print(total)