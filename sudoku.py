#import things
import os

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


#housekeeping
is_this_correct = 0

#welcome the user
os.system('cls' if os.name == 'nt' else 'clear')
print("Welcome to sudoku solver." + "\n" + "\n" + "First you will put in the numbers in the right places." + "\n" + "\n" + "Then I will solve the sudoku and tell you the answer." + "\n" + "\n" + "To put in number first put in the column, then the row, lastly put in the number you want it to be." + "\n" + "\n" + "You don't have to fill all the spots, just leave them blank if they don't have anything in them." + "\n" + "\n" + "To reset a spot just put in a 0." + "\n" + "\n" + "After puting in all the number press enter to check them." + "\n")
input(f"press enter to contiune: ")

#make the grid
grid = [[" " for _ in range(9)] for _ in range(9)]
grid_two = [[" " for _ in range(9)] for _ in range(9)]

#print the result of the changes
os.system('cls' if os.name == 'nt' else 'clear')

print(f"     1   2   3     4   5   6     7   8   9")
#print the grid as it is now
for i in range(9):
    if (i + 1) % 3 == 0:
        print(f"    ___ ___ ___   ___ ___ ___   ___ ___ ___\n {i + 1} | {grid[i][0]} | {grid[i][1]} | {grid[i][2]} | | {grid[i][3]} | {grid[i][4]} | {grid[i][5]} | | {grid[i][6]} | {grid[i][7]} | {grid[i][8]} | \n    ___ ___ ___   ___ ___ ___   ___ ___ ___") 
    else:
        print(f"    ___ ___ ___   ___ ___ ___   ___ ___ ___\n {i + 1} | {grid[i][0]} | {grid[i][1]} | {grid[i][2]} | | {grid[i][3]} | {grid[i][4]} | {grid[i][5]} | | {grid[i][6]} | {grid[i][7]} | {grid[i][8]} |")
 


#get the sudoku from the player
while is_this_correct != "1":
    number = 0

    #whilr the player is puting in points:
    while type(number) != str:

        #get the point and where it is going
        number = input("Enter the column it's on first, then the row, and then the number you want it to be.(to reset a number put in a 0): ")

        #split number up
        point = [str(digit) for digit in str(number)]
        #if is is three points do this
        if len(point) >= 3:
            #resest number
            number = 0
            #find and place the number
            grid[int(point[1]) - 1][int(point[0]) - 1] = point[2]

            #clear the screen
            os.system('cls' if os.name == 'nt' else 'clear')

            print(f"     1   2   3     4   5   6     7   8   9")
            #print the grid as it is now
            for i in range(9):
                if (i + 1) % 3 == 0:
                    print(f"    ___ ___ ___   ___ ___ ___   ___ ___ ___\n {i + 1} | {grid[i][0]} | {grid[i][1]} | {grid[i][2]} | | {grid[i][3]} | {grid[i][4]} | {grid[i][5]} | | {grid[i][6]} | {grid[i][7]} | {grid[i][8]} | \n    ___ ___ ___   ___ ___ ___   ___ ___ ___") 
                else:
                    print(f"    ___ ___ ___   ___ ___ ___   ___ ___ ___\n {i + 1} | {grid[i][0]} | {grid[i][1]} | {grid[i][2]} | | {grid[i][3]} | {grid[i][4]} | {grid[i][5]} | | {grid[i][6]} | {grid[i][7]} | {grid[i][8]} |")
 

        #else set number to a str
        else: 
            number = " "

    #clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    #print the grid as it is now
    for i in range(9):
        if (i + 1) % 3 == 0:
            print(f"  ___ ___ ___   ___ ___ ___   ___ ___ ___\n | {grid[i][0]} | {grid[i][1]} | {grid[i][2]} | | {grid[i][3]} | {grid[i][4]} | {grid[i][5]} | | {grid[i][6]} | {grid[i][7]} | {grid[i][8]} | \n  ___ ___ ___   ___ ___ ___   ___ ___ ___") 
        else:
            print(f"  ___ ___ ___   ___ ___ ___   ___ ___ ___\n | {grid[i][0]} | {grid[i][1]} | {grid[i][2]} | | {grid[i][3]} | {grid[i][4]} | {grid[i][5]} | | {grid[i][6]} | {grid[i][7]} | {grid[i][8]} |")
 

    #ask if they want to change it more
    is_this_correct = input("is this the board you want to use, 1 for yes 0 for no: ")

#set the grid up
for x in range(9):
    for y in range(9):
        if grid[x][y] != " " and grid[x][y] != 0 and len(grid[x][y]) < 2:
            grid[x][y] = int(grid[x][y])
            grid_two[x][y] = int(grid[x][y])
        else:
            grid[x][y] = int(0)
            grid_two[x][y] = int(0)

#clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

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
    os.system('cls' if os.name == 'nt' else 'clear')

    #print the grid as it is now
    for i in range(9):
        if (i + 1) % 3 == 0:
            print(f"  ___ ___ ___   ___ ___ ___   ___ ___ ___\n | {grid[i][0]} | {grid[i][1]} | {grid[i][2]} | | {grid[i][3]} | {grid[i][4]} | {grid[i][5]} | | {grid[i][6]} | {grid[i][7]} | {grid[i][8]} | \n  ___ ___ ___   ___ ___ ___   ___ ___ ___") 
        else:
            print(f"  ___ ___ ___   ___ ___ ___   ___ ___ ___\n | {grid[i][0]} | {grid[i][1]} | {grid[i][2]} | | {grid[i][3]} | {grid[i][4]} | {grid[i][5]} | | {grid[i][6]} | {grid[i][7]} | {grid[i][8]} |")
#else say ir can't be solved

else:
    #clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    #print the message
    print(f"This sudoku cann't be solved")
