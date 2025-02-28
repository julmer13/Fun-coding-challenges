#import things
import os
import random

#global varuables 
grid_spaces = "  "
bombs_symbol = "#"

#def things
def make_colors(text, color):
    colors = {  
        "white":"\33[47m",
        "reset": "\033[0m",
        "grey": "\033[100m"
    }
    return f"{colors[color]}{text}{colors['reset']}"

def make_map_for_winning(size, Number_of_bombs, grid):
    Bombs_places = []
    while len(Bombs_places) < Number_of_bombs:
        for _ in range(Number_of_bombs - (len(Bombs_places))):
            random_x = random.randint(0, size - 1)
            random_y = random.randint(0, size - 1)
            if [random_x, random_y] not in Bombs_places:
                grid[random_y][random_x] = bombs_symbol
                Bombs_places.append([random_x, random_y])
    for bomb in Bombs_places:
        x, y = bomb
        for new_x in range(x - 1, x + 2):
            for new_y in range(y - 1, y + 2):
                if new_x < 0 or new_x >= size or new_y < 0 or new_y >= size:
                    continue
                if grid[new_y][new_x] != bombs_symbol:
                    if grid[new_y][new_x] == grid_spaces:
                        grid[new_y][new_x] = 1
                    else:
                        grid[new_y][new_x] = grid[new_y][new_x] + 1
    for check_x in range(0, size):
        for check_y in range(0, size):
            if grid[check_y][check_x] != grid_spaces:
                grid[check_y][check_x] = str(grid[check_y][check_x]).center(len(grid_spaces))
            if (check_x + check_y) % 2 == 1:
                grid[check_y][check_x] = make_colors(grid[check_y][check_x], "grey")

    return Bombs_places

