import os
import re

path = os.path.dirname(os.path.realpath(__file__))
input = ""
sum = 0

cards = {}
cardscount = {}

with open(os.path.join(path,'input.txt')) as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()

    print(line)
    matches = re.match("Card\s+(\d+):\s+([\d\s]+)\s+\|\s+([\d\s]+)", line)

    cardid = matches.group(1)
    cardwins = re.findall("(\d+)", matches.group(2))
    cardnums = re.findall("(\d+)", matches.group(3))

    cards.update({cardid : {
        "wins" : cardwins,
        "nums" : cardnums
    }})
    
    cardscount.update({cardid: 1})

for cardid, cardcount in cardscount.items():
    wins = 0
    print("Card {}: Count: {}".format(cardid, cardcount))
    
    card = cards.get(cardid)
    
    for num in card.get("nums"):
        if num in card.get("wins"):
            wins = wins + 1
    
    print("Card {}: Wins {}".format(cardid, wins))
    
    for c in range(0, cardcount):
        for i in range(int(cardid)+1, int(cardid)+wins+1):            
            cardscount.update({str(i) : cardscount.get(str(i))+1})
    
    sum = sum + cardcount
    
    print("---")

print('final sum: ' + str(sum))