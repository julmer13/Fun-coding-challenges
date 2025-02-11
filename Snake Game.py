#import things
import time
import sys
import tty
import termios
import select
import os

#def things
def move_snake(curent_place_x, curent_place_y, direction, grid, places):
    if direction == "up":
        grid[curent_place_y - 1][curent_place_x] = "#"
        places.append(curent_place_x)
        places.append(curent_place_y - 1)
    if direction == "down":
        grid[curent_place_y + 1][curent_place_x] = "#"
        places.append(curent_place_x)
        places.append(curent_place_y + 1)
    if direction == "left":
        grid[curent_place_y][curent_place_x - 1] = "#"
        places.append(curent_place_x - 1)
        places.append(curent_place_y )
    if direction == "right":
        grid[curent_place_y][curent_place_x + 1] = "#"
        places.append(curent_place_x + 1)
        places.append(curent_place_y)

def get_key(timeout):
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        # Use select to check if there's input available
        rlist, _, _ = select.select([sys.stdin], [], [], timeout)
        if rlist:
            key = sys.stdin.read(3)  # Read 3 bytes (for arrow keys)
        else:
            key = None
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key

move = "up"
grid = [[" " for _ in range(20)] for _ in range(20)]
speed = 0.5
grid[5][4] = "#"
current_places = [4, 5]
for row in grid:
    #print the grid
    print(row)

while True:
    start_time = time.perf_counter()
    key = get_key(speed)
    if key == '\x1b[A':
        move_snake(current_places[-2], current_places[-1], "up", grid, current_places)
        move = "up"
    elif key == '\x1b[B':
        move_snake(current_places[-2], current_places[-1], "down", grid, current_places)
        move = "down"
    elif key == '\x1b[D':
        move_snake(current_places[-2], current_places[-1], "left", grid, current_places)
        move = "left"
    elif key == '\x1b[C':
        move_snake(current_places[-2], current_places[-1], "right", grid, current_places)
        move = "right"
    else:
        move_snake(current_places[-2], current_places[-1], move, grid, current_places)

    end_time = time.perf_counter()
    if end_time - start_time < speed:
        time.sleep(speed - (end_time - start_time))
    
    if len(current_places) // 2 > 4:
        tail_x = current_places.pop(0)
        tail_y = current_places.pop(0)
        grid[tail_y][tail_x] = " "

    os.system('cls' if os.name == 'nt' else 'clear')

    for row in grid:
        #print the grid
        print(row)
    print( )