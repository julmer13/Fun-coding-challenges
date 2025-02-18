#import things
import os
import time
import random
import shutil

#def things here
def random_color(round):
    if round > 6:
        possible_colors = 7
    elif round > 4:
        possible_colors = 6
    elif round > 2:
        possible_colors = 5
    else:
        possible_colors = 4
    
    color = random.randint(1, possible_colors)
    if color <= 4:
        return (color,)
    if color == 5:
        return random.randint(1, 4), random.randint(1, 4)
    if color == 6:
        return random.randint(1, 4), random.randint(1, 4), random.randint(1, 4)
    if color == 7:
        return random.randint(1, 4), random.randint(1, 4), random.randint(1, 4), random.randint(1, 4)
    
def get_ter_size():
    ter_size = shutil.get_terminal_size(fallback=(80, 24))
    if ter_size.columns < ter_size.lines:
        if ter_size.columns % 2 == 0:
            return ter_size.columns - 3
        else:
            return ter_size.columns - 1
    else:
        if ter_size.lines % 2 == 0:
            return (ter_size.lines - 3)
        else:
            return ter_size.lines - 1
        
def make_color(text, color):
    colors = {
        "green": "\033[42m",
        "red": "\033[41m",  
        "white": "\33[47m",
        "reset": "\033[0m",
        "blue": "\033[46m", 
        "yellow": "\033[43m"  
    }
    return f"{colors[color]}{text}{colors['reset']}"
    
def show_color(round, grid):
    colors_to_print = list(random_color(round))
    for i in range(len(colors_to_print)):
        if colors_to_print[i] == 1:
            color = "red"
            for y in range(0, (len(grid) // 2) - 1):
                for x in range((len(grid) // 2) + 1, len(grid)):
                    grid[y][x] = make_color(grid[y][x], color)
        elif colors_to_print[i] == 2:
            color = "blue"
            for y in range((len(grid) // 2) + 1, len(grid)):
                for x in range((len(grid) // 2) + 1, len(grid)):
                    grid[y][x] = make_color(grid[y][x], color)
        elif colors_to_print[i] == 3:
            color = "yellow"
            for y in range((len(grid) // 2) + 1, len(grid)):
                for x in range(0, (len(grid) // 2) - 1):
                    grid[y][x] = make_color(grid[y][x], color)
        elif colors_to_print[i] == 4:
            color = "green"
            for y in range(0, (len(grid) // 2) - 1):
                for x in range(0, (len(grid) // 2) - 1):
                    grid[y][x] = make_color(grid[y][x], color)

os.system('cls' if os.name == 'nt' else 'clear')
grid = [["  " for _ in range(get_ter_size())] for _ in range(get_ter_size())]
for x in range(0, len(grid)):
    grid[(len(grid) // 2) - 1][x] = make_color(grid[(len(grid) // 2) - 1][x], "white")
    grid[(len(grid) // 2)][x] = make_color(grid[len(grid) // 2][x], "white")
for y in range(0, len(grid)):
    grid[y][(len(grid) // 2) - 1] = make_color(grid[y][(len(grid) // 2) - 1], "white")
    grid[y][(len(grid) // 2)] = make_color(grid[y][(len(grid) // 2)], "white")

show_color(10, grid)
for row in grid:
    print("".join(row))