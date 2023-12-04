import os
import re

path = os.path.dirname(os.path.realpath(__file__))
input = ""
sum = 0

with open(os.path.join(path,'input.txt')) as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()

    print(line)
    matches = re.match("Card\s+(\d+):\s+([\d\s]+)\s+\|\s+([\d\s]+)", line)

    cardid = matches.group(1)
    cardwins = re.findall("(\d+)", matches.group(2))
    cardnums = re.findall("(\d+)", matches.group(3))

    wins = 0

    for num in cardnums:
        if num in cardwins:
            wins = wins + 1

    points = 0

    if wins > 0:
        points = pow(2, wins-1)
        sum = sum + points
    
    print("Card {}: Wins {}, Points {}".format(cardid, wins, points))

print('final sum: ' + str(sum))