# CHALLENGE PROBLEM: 
#
# Use your check_sudoku function as the basis for solve_sudoku(): a
# function that takes a partially-completed Sudoku grid and replaces
# each 0 cell with an integer in the range 1..9 in such a way that the
# final grid is valid.
#
# There are many ways to cleverly solve a partially-completed Sudoku
# puzzle, but a brute-force recursive solution with backtracking is a
# perfectly good option. The solver should return None for broken
# input, False for inputs that have no valid solutions, and a valid
# 9x9 Sudoku grid containing no 0 elements otherwise. In general, a
# partially-completed Sudoku grid does not have a unique solution. You
# should just return some member of the set of solutions.
#
# A solve_sudoku() in this style can be implemented in about 16 lines
# without making any particular effort to write concise code.

import random

# solve_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return valid unchanged
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return a 
# sudoku grid which passes a 
# sudoku checker. There may be
# multiple correct grids which 
# can be made from this starting 
# grid.
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]
        
easySolve = [[2, 9, 4, 5, 6, 3, 1, 7, 8],
             [3, 1, 6, 7, 2, 8, 4, 9, 5],
             [8, 5, 7, 1, 4, 9, 6, 3, 2],
             [6, 2, 9, 4, 3, 1, 5, 8, 7],
             [5, 7, 3, 6, 8, 2, 9, 1, 4],
             [1, 4, 8, 9, 5, 7, 2, 6, 3],
             [7, 6, 5, 3, 9, 4, 8, 2, 1], 
             [9, 8, 1, 2, 7, 5, 3, 4, 6],
             [4, 3, 2, 8, 1, 6, 0, 5, 9]]


# Note: this may timeout 
# in the Udacity IDE! Try running 
# it locally if you'd like to test 
# your solution with it.
# 
hard = [[1,0,0,0,0,7,0,9,0],
         [0,3,0,0,2,0,0,0,8],
         [0,0,9,6,0,0,5,0,0],
         [0,0,5,3,0,0,9,0,0],
         [0,1,0,0,8,0,0,0,2],
         [6,0,0,0,0,4,0,0,0],
         [3,0,0,0,0,0,0,1,0],
         [0,4,0,0,0,0,0,0,7],
         [0,0,7,0,0,0,3,0,0]]

def review(grid):
    #Size grid
    if len(grid) == 0:
        return False        
    #Size 9x9
    for row in grid:
        if len(row) != 9:
            return None
    #Row check
    for row in grid:
        aux = []
        for element in row:
            if element in aux:
                if element != 0:
                    return False
            else:
                aux.append(element)
    #Column check
    for i in range(0,len(grid)):
        aux = []
        for j in range(0,len(grid)):
            if grid[j][i] in aux:
                if grid[j][i] != 0:
                    return False
            else:
                aux.append(grid[j][i])
    #3x3 check
    for k in range(0,9,3):
        for l in range(0,9,3):
            aux = []
            for i in range(k, k+3):
                for j in range(l, l+3):
                   aux.append(grid[i][j])
            aux2 = []
            for element in aux:
                if element in aux2:
                    if element != 0:
                        return False
                else:
                    aux2.append(element)
    return True

def check_sudoku(grid):
    ###Your code here.
    return review(grid)


def printGrid(grid):
    for row in grid:
        print row
#
# This function proves if the grid is fulfilled
# Return false if not and give us the row and the column values
#
def findUnassignedField(grid):
    for i in range(0, 9):
        for j in range(0, 9):
            if grid[i][j] == 0:
                return True, i, j
    return False, i, j

def solve_sudoku (grid):
    ###Your code here.
    
    prueba, row, column = findUnassignedField(grid)
    
    print row, column, prueba
    
    if not prueba:
        return True
    
    for num in range(1, 10):
        if(check_sudoku(grid)):
            grid[row][column] = num
            if check_sudoku(grid) and solve_sudoku (grid):
                return True
            grid[row][column] = 0
    return False


#printGrid(easy)
#solve_sudoku(easy)
#printGrid(easy)
#check_sudoku(easy)

printGrid(hard)
solve_sudoku(hard)
printGrid(hard)
print(check_sudoku(hard))