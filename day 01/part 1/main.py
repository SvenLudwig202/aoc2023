import os
import io
import re

path = os.path.dirname(os.path.realpath(__file__))
input = ""
sum = 0

with open(os.path.join(path,'input.txt')) as f:
    input = f.read()

lines = io.StringIO(input)

for line in lines:
    line = line.strip()
    digits = re.findall('\d', line)
    digits = ''.join(digits)
    
    solution = ''.join(digits[0] + digits[-1])
    sum = sum + int(solution)
    
    print(
        line + ' - ' +
        digits + ' - ' +
        solution + ' - ' +
        str(sum)
        )
    
print('final sum: ' + str(sum))