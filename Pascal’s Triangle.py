#import things
import math

#def things

#get number based on row and positation
def get_number(row, position):
    return int(math.factorial(row) / (math.factorial(position) * math.factorial(row - position)))

#run a method to get the right numbers
def fill_row(row, grid, max_digits):
    #check if the row is to low
    if row >= 1:
        #run through all grid position in a row
        for number in range(row):
            #update the grid
            grid[row - 1][number] = str(get_number(row - 1, number)).center(max_digits)
        #run it again on a lower row
        fill_row(row - 1, grid, buffer_number)
        #return the grid
        return grid
    #return none to start the chain back
    else:
        return None
    
#make the empty grid to start
def empty_grid(rows):
    #make start empty grid
    grids = []
    #make each row one by one
    for spaces in range(rows):
        #add a list the is the right length
        grids.append(["#" for _ in range(spaces + 1)])
    #return the grid
    return grids

#main program/clear screen
print("\033c", end="")

try:
    while True:

        #define starting values
        biggest_row = int(input(f"Give me the largest row of Pascal's triangle and I will give you the whole triangle: ")) #starting row
        buffer_number = len(str(get_number(biggest_row, biggest_row // 2)))

        #reclear the screen
        print("\033c", end="")

        #make and fill the grid of numbers
        grid = empty_grid(biggest_row)
        grid = fill_row(biggest_row, grid, buffer_number)

        #get the len of the final row
        finale_buffer = len(" ".join(grid[len(grid) - 1]))

        #print the result
        for line in grid:
            print((" ".join(line)).center(finale_buffer))

#add a expect statment
except KeyboardInterrupt:
    print("program ended") 