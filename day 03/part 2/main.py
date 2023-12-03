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

def getnumber(row, col):  
    number = grid[row, col]
    
    lcol = col
    rcol = col
    
    while True:
        lcol = lcol - 1
        
        if lcol >= limit_rowmin:
            value = grid[row, lcol]
            if value.isnumeric():
                number = value + number
            else:
                break
        else:
            break
    
    while True:
        rcol = rcol + 1
        
        if rcol < limit_rowmax:
            value = grid[row, rcol]
            if value.isnumeric():
                number = number + value
            else:
                break
        else:
            break
    
    return number
            

def getsurroundingnumbers(row, col):
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
    
    numbers = []
    
    for srow, scol in surrounds:
        if srow in limit_row and scol in limit_col:
            value = grid[srow, scol]
            if (value.isnumeric()):
                numbers += [[srow, getnumber(srow, scol)]]
    
    return numbers

number = ""
valid = False

for (row, col), value in np.ndenumerate(grid):
    if (value == '*'):
        print(row, col, value)
        values = np.unique(getsurroundingnumbers(row, col), axis=0)
        if (len(values) == 2):
            a = int(values[0][1])
            b = int(values[1][1])
            
            print(a, b, a*b)
            sum = sum + a*b
    
print('final sum: ' + str(sum))