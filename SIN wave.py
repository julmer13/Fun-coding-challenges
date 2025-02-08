#import things
import os
import time

#def things
def first_wave(number_list, len_of_list):
    new_list = []
    while len(new_list) < len_of_list:
        for i in range(0, 2):
            for number in number_list:
                if len(new_list) < len_of_list:
                    if i == 1:
                        new_list.append(number)
                    else:
                        new_list.append(number * -1)
    return new_list

def next_wave(number_list, new_number, first_list):
    new_number = first_list[new_number]
    new_list = [0]
    for i in range(0, len(number_list) - 1, 1):
        new_list.append(number_list[i])
    new_list[0] = new_number * -1

    return new_list

def move_bars(grid, new_number, first_list, length):
    new_number_to_use = first_list[new_number % len(first_list)]
    midpoint = len(grid) // 2
    for y in range(length):  
        for x in range(len(grid[0]) - 1, 2, -1): 
            grid[y][x] = grid[y][x - 1]

    for y in range(length):
        grid[y][2] = " " 
    
    bar_height = abs(new_number_to_use)

    if new_number_to_use < 0:
        for y in range(midpoint - 1, midpoint - bar_height - 1, -1):
            grid[y][2] = "#"
    if new_number_to_use > 0:
        for y in range(midpoint + 1, midpoint + bar_height + 1):
            grid[y][2] = "#"

    grid[midpoint][2] = "-"

#clear the screen and welcome the user
os.system('cls' if os.name == 'nt' else 'clear')
input_number = int(input(f"Give me the top/bottom value for a wave of numbers: "))
list_size = int(input(f"What size do you want the list to be: "))
speed = float(input(f"how fast do you want the numbers to go acroos the screen: "))

list_of_possible_numbers = []
grid = [[" " for _ in range(list_size + 2)] for _ in range((input_number * 2) + 1)]

for i in range(input_number, -1, -1):
    list_of_possible_numbers.append(input_number - i)
for i in range(1, input_number):
    list_of_possible_numbers.append(input_number - i)

numbers_to_use = first_wave(list_of_possible_numbers, len(list_of_possible_numbers) * 2)

starting_list = first_wave(list_of_possible_numbers, list_size)
changing_list = starting_list

spaces_needed = len(str(input_number)) + 1

for y in range(len(grid)):
    grid[y][1] = "|"
    if y > input_number:
        grid[y][0] = str(input_number + (y * -1)).rjust(spaces_needed)
    else:
        grid[y][0] = str(input_number + (y * -1)).rjust(spaces_needed)

gap = " " * spaces_needed

for times in range((list_size // input_number) + 2):
    for i in range(-1, (len(numbers_to_use) * -1) - 1, -1):
        move_bars(grid, i, numbers_to_use, len(grid))
        changing_list = next_wave(changing_list, i, numbers_to_use)

try:
    while True:
        for i in range(-1, (len(numbers_to_use) * -1) - 1, -1):
            os.system('cls' if os.name == 'nt' else 'clear')

            for row in grid:
                print(gap.join(row))

            string_list = [str(num).center(spaces_needed) for num in changing_list]
            print(gap + gap + gap +  " ".join(string_list))

            time.sleep(speed)

            move_bars(grid, i, numbers_to_use, len(grid))
            changing_list = next_wave(changing_list, i, numbers_to_use)

except KeyboardInterrupt:
    print("program stopped")