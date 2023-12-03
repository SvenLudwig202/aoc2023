import os
import re
import numpy as np

path = os.path.dirname(os.path.realpath(__file__))
input = ""
sum = 0

grid = np.array([])

with open(os.path.join(path,'input.txt')) as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    
    if (grid.size == 0):
        grid = np.array([*line])
    else:
        grid = np.vstack([grid, [*line]])

print(grid)

limit_rowmin = 0
limit_rowmax = grid.shape[0]
limit_row = range(limit_rowmin, limit_rowmax)
limit_colmin = 0
limit_colmax = grid.shape[1]
limit_col = range(limit_colmin, limit_colmax)

def hasadjacentsymbol(row, col, grid):
    surrounds = [
        [row-1, col-1],
        [row-1, col],
        [row-1, col+1],
        [row,   col-1],
        [row,   col+1],
        [row+1, col-1],        
        [row+1, col],
        [row+1, col+1]
    ]
    
    for srow, scol in surrounds:
        if srow in limit_row and scol in limit_col:
            value = grid[srow, scol]
            if (not value.isnumeric() and value != '.'):
                return True
    
    return False

number = ""
valid = False

for (row, col), value in np.ndenumerate(grid):
    if (value.isnumeric()):
        number = number + value
        if (hasadjacentsymbol(row, col, grid)):
            valid = True
            
    if (number == '617'):
        pass
    
    if (not value.isnumeric() or col == limit_colmax-1):
        if len(number) > 0:
            if (valid == True):
                sum = sum + int(number)
            
            print(number, valid)
            number = ""
            valid = False
    
print('final sum: ' + str(sum))