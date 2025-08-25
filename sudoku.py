# imports
import pandas as pd
import numpy as np
from pathlib import Path

#def things
def colorizer(n):
    colors = {
        "red": "\033[31m",  
        "reset": "\033[0m",
    }
    return f"{colors['red']}{n}{colors['reset']}"

def is_valid_board():
    #for all the rows
    for row in grid:
        #all the number it can be
        numbers_left = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #make the m
        for m in range(0, len(row)):
            #try this:
            try:
                if row[m] != 0:
                    numbers_left.remove(row[m])
            #except if the number is not in numbers left
            except ValueError:
                return False

    #for all the col in grid    
    for col in range(9):
        #all the number it can be
        numbers_left = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #make a m
        for m in range(9):
            #try this:
            try:
                if grid[m][col] != 0:
                    numbers_left.remove(grid[m][col])
            #except if the number is not in number left
            except ValueError:
                return False

    #go through all the mini grids
    x1 = 0 #set the offset for the x
    y1 = 0 #set the offset for the y

    #go though all the sub grids
    for m in range(9):
        #set the sub grid
        mini_grid = [[" " for _ in range(3)] for _ in range(3)]
        #set the number so it can't repeat
        numbers_left = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #go through the y
        for y in range(3):
            #go through the x
            for x in range(3):
                #set that position in the sub grid
                mini_grid[x][y] = grid[x + x1][y + y1]
                #try this
                try:
                    #check that the spot is not a 0 first
                    if mini_grid[x][y] != 0:
                        #remove its value from the numbers left
                        numbers_left.remove(mini_grid[x][y])
                #if Error return false
                except ValueError:
                    return False
        #change the offshoots
        x1 += 3
        if x1 > 6:
            x1 = 0
            y1 +=3

    #if all that makes it through return true
    return True

def is_valid(grid, row, col, num):
    # Check the row
    if num in grid[row]:
        return False

    # Check the column
    if num in [grid[i][col] for i in range(9)]:
        return False

    # Check the 3x3 subgrid
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def solve_it():
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_it():
                            return True
                        grid[row][col] = 0  # Undo move if it leads to a dead end
                return False  # No number fits, trigger backtracking
    return True  # All cells are filled

# === Excel load (reads 11x11 with separator rows/cols at 4 and 8; blanks->0 in memory) ===
excel_path = str(Path(__file__).with_name("Soduko.xlsx"))
df_raw = pd.read_excel(excel_path, header=None)

# keep rows/cols (zero-based) 0,1,2,4,5,6,8,9,10  (skip 3 and 7)
keep = [0, 1, 2, 4, 5, 6, 8, 9, 10]
df_sel = df_raw.iloc[keep, keep].copy()

# convert to numeric; non-numeric -> NaN
num = pd.to_numeric(df_sel.stack(), errors="coerce").unstack()

# blanks -> 0 for solver
num = num.fillna(0).astype(int)

#make the grid from Excel
grid = num.values.tolist()
grid_two = [row[:] for row in grid]

#housekeeping
is_this_correct = "1"   # skip manual entry since we’re loading from Excel

#welcome the user
print("\033c", end="")
print("Welcome to sudoku solver.\n\nLoaded puzzle from Soduko.xlsx.\n")

#print the result of the changes
print("\033c", end="")

print(f"     1   2   3     4   5   6     7   8   9")
for i in range(9):
    if (i + 1) % 3 == 0:
        print(f"    ___ ___ ___   ___ ___ ___   ___ ___ ___\n {i + 1} | {grid[i][0]} | {grid[i][1]} | {grid[i][2]} | | {grid[i][3]} | {grid[i][4]} | {grid[i][5]} | | {grid[i][6]} | {grid[i][7]} | {grid[i][8]} | \n    ___ ___ ___   ___ ___ ___   ___ ___ ___") 
    else:
        print(f"    ___ ___ ___   ___ ___ ___   ___ ___ ___\n {i + 1} | {grid[i][0]} | {grid[i][1]} | {grid[i][2]} | | {grid[i][3]} | {grid[i][4]} | {grid[i][5]} | | {grid[i][6]} | {grid[i][7]} | {grid[i][8]} |")

# (manual input block removed since we’re using Excel)

#clear the screen
print("\033c", end="")

#print the grid as it is now
for i in range(9):
    if (i + 1) % 3 == 0:
        print(f"  ___ ___ ___   ___ ___ ___   ___ ___ ___\n | {grid[i][0]} | {grid[i][1]} | {grid[i][2]} | | {grid[i][3]} | {grid[i][4]} | {grid[i][5]} | | {grid[i][6]} | {grid[i][7]} | {grid[i][8]} | \n  ___ ___ ___   ___ ___ ___   ___ ___ ___") 
    else:
        print(f"  ___ ___ ___   ___ ___ ___   ___ ___ ___\n | {grid[i][0]} | {grid[i][1]} | {grid[i][2]} | | {grid[i][3]} | {grid[i][4]} | {grid[i][5]} | | {grid[i][6]} | {grid[i][7]} | {grid[i][8]} |")
    
#add a solving screen
print(f"Solving...")

#if it can be solved:
if solve_it() and is_valid_board():
    #colorizer it
    for x in range(9):
        for y in range(9):
            if grid[x][y] != grid_two[x][y]:
                grid[x][y] = colorizer(grid[x][y])

    #clear the screen
    print("\033c", end="")

    #print the grid as it is now
    for i in range(9):
        if (i + 1) % 3 == 0:
            print(f"  ___ ___ ___   ___ ___ ___   ___ ___ ___\n | {grid[i][0]} | {grid[i][1]} | {grid[i][2]} | | {grid[i][3]} | {grid[i][4]} | {grid[i][5]} | | {grid[i][6]} | {grid[i][7]} | {grid[i][8]} | \n  ___ ___ ___   ___ ___ ___   ___ ___ ___") 
        else:
            print(f"  ___ ___ ___   ___ ___ ___   ___ ___ ___\n | {grid[i][0]} | {grid[i][1]} | {grid[i][2]} | | {grid[i][3]} | {grid[i][4]} | {grid[i][5]} | | {grid[i][6]} | {grid[i][7]} | {grid[i][8]} |")

    # === reset Excel AFTER success: numbers -> 0, blanks preserved; separators stay blank ===
    reset_raw = df_raw.copy()
    for ri, r in enumerate(keep):
        for ci, c in enumerate(keep):
            val = pd.to_numeric(df_sel.iat[ri, ci], errors="coerce")
            reset_raw.iat[r, c] = 0 if not pd.isna(val) else np.nan

    with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
        reset_raw.to_excel(writer, index=False, header=False)

#else say it can't be solved
else:
    print("\033c", end="")
    print(f"This sudoku cann't be solved")