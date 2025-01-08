#import things
import math
import os

#clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

#def things
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

try:
    #main program
    while True:
        #house keeping 
        number = 2

        #get the grid size
        while number % 2 == 0: 
            number = int(input("How big do you want the grid to be? Please enter an odd number: "))
            prime_sign = str(input(f"What do you want the primes to look like: "))
            other_sign = str(input(f"What do you want the other numbers look like: "))

        #make grid for 1 - number
        rows, cols = number, number
        grid = [[0 for _ in range(cols)] for _ in range(rows)]

        current_value = number * number  # Start with the highest number

        # Start filling the spiral from the bottom-right corner
        for i in range((number + 1) // 2):  # Number of layers in the spiral
            # Bottom row (right to left)
            for x in range(number - 1 - i, i - 1, -1):
                grid[number - 1 - i][x] = current_value
                current_value -= 1

            # Left wall (bottom to top)
            for y in range(number - 2 - i, i - 1, -1):
                grid[y][i] = current_value
                current_value -= 1

            current_value += 1

            # Top row (left to right)
            for x in range(i, number - i):
                grid[i][x] = current_value
                current_value -= 1

            # Right wall (top to bottom)
            for y in range(i + 1, number - 1 - i):
                grid[y][number - 1 - i] = current_value
                current_value -= 1

        #change each number to be prime or not
        for h in range(0, number):
            for e in range(0, number):
                if grid[h][e] == 1:
                    grid[h][e] = '\033[31m#\033[0m'
                elif is_prime(grid[h][e]):
                    grid[h][e] = prime_sign
                else:
                    grid[h][e] = other_sign


        #clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')

        for row in grid:
            #print the grid
            print(" ".join(row))

except KeyboardInterrupt:
    print("program ended")

#good ones: mac 271 at max - 1 zoom
#chroombook: 87 at 50% zoom