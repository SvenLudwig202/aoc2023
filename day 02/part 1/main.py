import os
import io
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
    
    invalid = False
    
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
                    if count > limit_red:
                        invalid = True
                case 'green':
                    if count > limit_green:
                        invalid = True
                case 'blue':
                    if count > limit_blue:
                        invalid = True
    
    if invalid == True:
        return 0
    else:
        return game

with open(os.path.join(path,'input.txt')) as f:
    input = f.read()

lines = io.StringIO(input)

for line in lines:
    line = line.strip()
    
    count = parseLine(line)
    
    if count > 0:
        print(line)
        print(count)
    
    sum = sum + count

print('final sum: ' + str(sum))