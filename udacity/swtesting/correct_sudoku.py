# SPECIFICATION:
#
# check_sudoku() determines whether its argument is a valid Sudoku
# grid. It can handle grids that are completely filled in, and also
# grids that hold some empty cells where the player has not yet
# written numbers.
#
# First, your code must do some sanity checking to make sure that its
# argument:
#
# - is a 9x9 list of lists
#
# - contains, in each of its 81 elements, an integer in the range 0..9
#
# If either of these properties does not hold, check_sudoku must
# return None.
#
# If the sanity checks pass, your code should return True if all of
# the following hold, and False otherwise:
#
# - each number in the range 1..9 occurs only once in each row 
#
# - each number in the range 1..9 occurs only once in each column
#
# - each number the range 1..9 occurs only once in each of the nine
#   3x3 sub-grids, or "boxes", that make up the board
#
# This diagram (which depicts a valid Sudoku grid) illustrates how the
# grid is divided into sub-grids:
#
# 5 3 4 | 6 7 8 | 9 1 2
# 6 7 2 | 1 9 5 | 3 4 8
# 1 9 8 | 3 4 2 | 5 6 7 
# ---------------------
# 8 5 9 | 7 6 1 | 4 2 3
# 4 2 6 | 8 5 3 | 7 9 1
# 7 1 3 | 9 2 4 | 8 5 6
# ---------------------
# 9 6 1 | 5 3 7 | 0 0 0
# 2 8 7 | 4 1 9 | 0 0 0
# 3 4 5 | 2 8 6 | 0 0 0
# 
# Please keep in mind that a valid grid (i.e., one for which your
# function returns True) may contain 0 multiple times in a row,
# column, or sub-grid. Here we are using 0 to represent an element of
# the Sudoku grid that the player has not yet filled in.

# check_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# check_sudoku should return True
hard = [[1,0,0,0,0,7,0,9,0],
        [0,3,0,0,2,0,0,0,8],
        [0,0,9,6,0,0,5,0,0],
        [0,0,5,3,0,0,9,0,0],
        [0,1,0,0,8,0,0,0,2],
        [6,0,0,0,0,4,0,0,0],
        [3,0,0,0,0,0,0,1,0],
        [0,4,0,0,0,0,0,0,7],
        [0,0,7,0,0,0,3,0,0]]

subg = [[9,8,7,6,5,4,3,2,1],
        [8,7,6,5,4,3,2,1,9],
        [7,6,5,4,3,2,1,9,8],
        [6,5,4,3,2,1,9,8,7],
        [5,4,3,2,1,9,8,7,6],
        [4,3,2,1,9,8,7,6,5],
        [3,2,1,9,8,7,6,5,4],
        [2,1,9,8,7,6,5,4,3],
        [1,9,8,7,6,5,4,3,2]]




def check_sudoku(grid):
    
    # Sanity checks
    
    if type(grid) is not list or len(grid) != 9:
        return None
       
    for row in grid:
        if len(row) != 9 or type(row) != list:
            return None
        
        for i in row:
            if type(i)!= int or i not in range(0,10):  
                return None     
    
    # Check only one in row 
    for row in grid:
        r = {}
        for d in row:
            if d not in r or d == 0:
                r[d] = 1
            else:
                return False
            
    # Check only digit in column
    for col in range(9):
        c = {}
        for row in grid:
            if row[col] not in c or row[col] == 0:
                c[row[col]] = 1
            else:
                return False
                           
    # Check cube
    for x in [0,3,6]:
        cube = {}
        for row in grid[x:x+3]:
 
            for d in row[x:x+3]:
                if d not in cube or d == 0:
                    cube[d] = 1
                else:
                    return False    
            
    return True



import copy

def solve_sudoku(__grid):
    
    res = check_sudoku(__grid)
    if res in [None, False]:
        return res
    
    copygrid = copy.deepcopy(__grid)

    for row in range(0,9):
        for col in range(0,9):
            if grid[row][col] == 0:
                for n in range(1,10):
                    grid[row][col] = n        
                    result = solve_sudoku(copygrid)
                    
                    if result is not False:
                        return result
                    
                return False              
    return copygrid    
                    
        

print 'subg',
#print check_sudoku(solve_sudoku(invalid))
result = solve_sudoku(subg)
print result

import sys
sys.exit(42)

print 'ill_formed',
print check_sudoku(solve_sudoku(ill_formed))


print 'valid',
print check_sudoku(solve_sudoku(valid))

print 'easy',
print check_sudoku(solve_sudoku(easy))

print 'hard',
print check_sudoku(solve_sudoku(hard))
        
print 'Finished!'