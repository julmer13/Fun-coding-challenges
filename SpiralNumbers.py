#import things
import math

#clear the screen
print("\033c", end="")

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
        "blue": "\033[36m",
        "red": "\033[31m",  
        "reset": "\033[0m",
    }
    return f"{colors[color]}{text}{colors['reset']}"

try:
    #main program
    while True:
        #house keeping 
        number = 2
        total = 0

        #get the grid size
        while number % 2 == 0: 
            number = int(input("How big do you want the grid to be? Please enter an odd number: "))


        #make grid for 1 - number
        rows, cols = number, number
        grid = [[0 for _ in range(cols)] for _ in range(rows)]

        current_value = number * number  # Start with the highest number
        total += current_value
        # Start filling the spiral from the bottom-right corner
        for i in range((number + 1) // 2):  # Number of layers in the spiral
            # Bottom row (right to left)
            for x in range(number - 1 - i, i - 1, -1):
                grid[number - 1 - i][x] = current_value
                current_value -= 1

            total += current_value + 1

            # Left wall (bottom to top)
            for y in range(number - 2 - i, i - 1, -1):
                grid[y][i] = current_value
                current_value -= 1

            current_value += 1

            total += current_value
            

            # Top row (left to right)
            for x in range(i, number - i):
                grid[i][x] = current_value
                current_value -= 1

            total += current_value + 1

            # Right wall (top to bottom)
            for y in range(i + 1, number - 1 - i):
                grid[y][number - 1 - i] = current_value
                current_value -= 1

            total += current_value

        #spaces needed
        spaces_needed = len(str(number * number))

        #change each number to the same lenth
        for h in range(0, number):
            for e in range(0, number):
                c = grid[h][e]
                new_number = str(c).center(spaces_needed)
                if c % 2 == 0:
                    grid[h][e] = colorize(new_number, "yellow")
                elif is_prime(c):
                    grid[h][e] = colorize(new_number, "blue")
                elif c == 1:
                    grid[h][e] = colorize(new_number, "red")
                else:
                    grid[h][e] = colorize(new_number, "green")

        #clear the screen
        print("\033c", end="")

        for row in grid:
            #print the grid
            print(" ".join(row))

        total -= 3
        print(f"The sum of the diagonals in this spiral is {total}")

except KeyboardInterrupt:
    print("program ended")