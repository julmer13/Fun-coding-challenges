#import things
import math
import os

#clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

#def things
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

# Function to colorize a number
def colorize(text, color):
    colors = {
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "reset": "\033[0m",
    }
    return f"{colors[color]}{text}{colors['reset']}"

try:
    #main program
    while True:
        number = int(input("How big do you want the triangle to be: "))

        #housekeeping 
        new_number = (number * 2) - 1

        #make grid for 1 - number
        rows, cols = number, new_number
        grid = [[0 for _ in range(cols)] for _ in range(rows)]

        current_number = 1

        for i in range(0, number):
            grid[i][int(((new_number + 1) / 2) - 1 - i)] = current_number
            current_number += 1

            if i != 0:
                for j in range(1, (i * 2) + 1):

                    grid[i][int(((new_number + 1) / 2) - 1 - i + j)] = current_number
                    current_number += 1

        # spaces_needed for formatting (based on the largest number in the grid)
        spaces_needed = len(str(number * number))

        # Format the grid with zero-padding
        for h in range(0, number):
            for e in range(0, new_number):
                c = grid[h][e]
                # If the cell is not zero, we format it; otherwise, we leave it as a blank space
                if c != 0:
                    # Apply zero-padding
                    grid[h][e] = str(c).zfill(spaces_needed)

                    # Colorize based on the value
                    if c % 2 == 0:  # Even numbers
                        grid[h][e] = colorize(grid[h][e], "yellow")
                    elif is_prime(c):  # Prime numbers
                        grid[h][e] = colorize(grid[h][e], "blue")
                    else:  # Odd numbers that are not prime
                        grid[h][e] = colorize(grid[h][e], "green")

                else:
                    grid[h][e] = ' ' * spaces_needed  # Create blank space for empty cells

        #clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')

        for row in grid:
            print(" ".join(row))

except KeyboardInterrupt:
    print("program ended")
