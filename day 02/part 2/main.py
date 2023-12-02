import os
import re

path = os.path.dirname(os.path.realpath(__file__))
input = ""
sum = 0

limit_red = 12
limit_green = 13
limit_blue = 14

def parseLine(txt):
    patternA = r"Game (\d+): (.*)"
    patternB = r"(\d+ \w+)"
    patternC = r"(\d+) (\w+)"
    
    max_red = 0
    max_green = 0
    max_blue = 0
    
    m = re.match(patternA, txt)
    
    game = int(m.group(1))
    draws = m.group(2).split('; ')
    
    for d in draws:
        cubes = re.findall(patternB, d)
        
        for c in cubes:
            m = re.match(patternC, c)
            count = int(m.group(1))
            color = m.group(2)
            
            match color:
                case 'red':
                    if count > max_red:
                        max_red = count
                case 'green':
                    if count > max_green:
                        max_green = count
                case 'blue':
                    if count > max_blue:
                        max_blue = count
    
    return max_red * max_green * max_blue

with open(os.path.join(path,'input.txt')) as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    
    count = parseLine(line)
    
    if count > 0:
        print(line)
        print(count)
    
    sum = sum + count

print('final sum: ' + str(sum))