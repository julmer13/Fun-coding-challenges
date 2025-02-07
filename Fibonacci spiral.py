#import things
import os

#def things
def Fibonacci_list_solver(Top_value):
    Fibonacci_list = []
    first_number = 1
    second_number = 1
    new_number = 0
    Fibonacci_list.append(first_number)
    Fibonacci_list.append(second_number)
    for t in range(Top_value - 2):
        new_number = first_number + second_number
        first_number = second_number
        second_number = new_number
        Fibonacci_list.append(new_number)
    return Fibonacci_list

#clear the screen and welcome the user
os.system('cls' if os.name == 'nt' else 'clear')
number = int(input("How big do you want the grid to be? Please enter an odd number: "))
number_list = Fibonacci_list_solver(number * number)

#make grid for 1 - number
rows, cols = number, number
grid = [[0 for _ in range(cols)] for _ in range(rows)]

current_value = number * number - 1  # Start with the highest number
# Start filling the spiral from the bottom-right corner
for i in range((number + 1) // 2):  # Number of layers in the spiral
    # Bottom row (right to left)
    for x in range(number - 1 - i, i - 1, -1):
        grid[number - 1 - i][x] = number_list[current_value]
        current_value -= 1

    # Left wall (bottom to top)
    for y in range(number - 2 - i, i - 1, -1):
        grid[y][i] = number_list[current_value]
        current_value -= 1

    current_value += 1
    
    # Top row (left to right)
    for x in range(i, number - i):
        grid[i][x] = number_list[current_value]
        current_value -= 1

    # Right wall (top to bottom)
    for y in range(i + 1, number - 1 - i):
        grid[y][number - 1 - i] = number_list[current_value]
        current_value -= 1

    spaces_needed = len(str(number_list[-1]))
    #change each number to the same lenth
    for h in range(0, number):
        for e in range(0, number):
            grid[h][e] = str(grid[h][e]).center(spaces_needed)

for row in grid:
    #print the grid
    print(" ".join(row))