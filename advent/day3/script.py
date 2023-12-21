import re

with open("data.txt", "r") as f:
    data = f.read()
lines = data.split('\n')

def is_symbol(char):
    return char != "." and not char.isdigit()

def complete_number(line, i):
    number = ""
    left = i
    right = i + 1

    while line[left].isnumeric():
        number += line[left]
        line = line[:left] + "." + line[left+1:]
        left -= 1
    number = number[::-1]

    try:
        while line[right].isnumeric():
            number += line[right]
            line = line[:right] + "." + line[right+1:]
            right += 1
    except:
        ...
    return int(number), line

total = 0

for count, line in enumerate(lines):
    symbol_matches = re.finditer(r'[^\.\d]', line)
    for match in symbol_matches:
        start = match.start()
        if line[start-1].isnumeric():
            total += complete_number(line, start-1)[0]
            line = complete_number(line, start-1)[1]
        elif line[start+1].isnumeric():
            total += complete_number(line, start+1)[0]
            line = complete_number(line, start+1)[1]

        prevline = lines[count-1]
        nextline = lines[count+1]

        if prevline[start].isnumeric():
            total += complete_number(prevline, start)[0]
            lines[count-1] = complete_number(prevline, start)[1]
        elif prevline[start-1].isnumeric():
            total += complete_number(prevline, start-1)[0]
            lines[count-1] = complete_number(prevline, start-1)[1]
        elif prevline[start+1].isnumeric():
            total += complete_number(prevline, start+1)[0]
            lines[count-1] = complete_number(prevline, start+1)[1]

        if nextline[start].isnumeric():
            total += complete_number(nextline, start)[0]
            lines[count+1] = complete_number(nextline, start)[1]
        elif nextline[start-1].isnumeric():
            total += complete_number(nextline, start-1)[0]
            lines[count+1] = complete_number(nextline, start-1)[1]
        elif nextline[start+1].isnumeric():
            total += complete_number(nextline, start+1)[0]
            lines[count+1] = complete_number(nextline, start+1)[1]

print(total)