import os
import io
import re

path = os.path.dirname(os.path.realpath(__file__))
input = ""
sum = 0

def findDigits(txt):
    ret = ''
    d = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
    }
    pattern = '|'.join(re.escape(k) for k in d)
    
    matches = re.findall(r'(?=({}))'.format(pattern), txt)
    
    for m in matches:
        ret = ret + d.get(m)
    
    return ret
    
with open(os.path.join(path,'input.txt')) as f:
    input = f.read()

lines = io.StringIO(input)

for line in lines:
    line = line.strip()
    
    orig = line
    
    digits = findDigits(line)
    
    solution = ''.join(digits[0] + digits[-1])
    sum = sum + int(solution)
    
    print(
        orig + ' - ' +
        line + ' - ' + 
        digits + ' - ' +
        solution + ' - ' +
        str(sum)
        )
    
print('final sum: ' + str(sum))