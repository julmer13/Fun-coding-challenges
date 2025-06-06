#import things
import shutil
from colorama import Fore, Style, Back, init
import time

#def things
def highlight_text(color, text):
    highlight_map = {
    "white": Back.WHITE,
    "gray": Back.LIGHTBLACK_EX
}
    color_code = highlight_map.get(color.lower(), Fore.RESET)
    return(f"{color_code}{text}{Style.RESET_ALL}")

sand = highlight_text("white", "  ")
empty_space = "  "

def get_terminal_size():
    ter_size = shutil.get_terminal_size(fallback=(80, 24)) 
    grid = [[empty_space for _ in range((ter_size.columns // 2) - 2)] for _ in range(ter_size.lines - 3)]
    return grid

def move_squares_down_one(grid):
    for line in range(len(grid) - 2, -1, -1):
        for i in range(len(grid[line])):
            if grid[line][i] == sand and grid[line + 1][i] == empty_space:
                grid[line + 1][i] = sand
                grid[line][i] = empty_space
    return grid

def print_with_border(grid):
    border_row = [highlight_text("gray", "  ") for _ in range(len(grid[0]) + 2)]
    grid_to_print = [border_row] + [[highlight_text("gray", "  ")] + row + [highlight_text("gray", "  ")] for row in grid] + [border_row]

    for row in grid_to_print:
        print("".join(row))

grid = get_terminal_size()
while True:
    time.sleep(0.1)
    print("\033c", end="")
    grid = move_squares_down_one(grid)
    print_with_border(grid)