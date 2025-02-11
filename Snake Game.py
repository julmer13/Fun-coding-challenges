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
        rlist, _, _ = select.select([sys.stdin], [], [], timeout)
        if rlist:
            key = sys.stdin.read(3) 
        else:
            key = None
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key

move = "non"
os.system('cls' if os.name == 'nt' else 'clear')
speed = float(input(f"what do you want the speed to be: "))
length = int(input(f"what do you want the length to be: "))
size = int(input(f"what do you want the size to be: "))
grid = [[" " for _ in range(size)] for _ in range(size)]
game_state = "wining"
grid[(size // 2) - 1][(size // 2) - 1] = "#"
current_places = [(size // 2) - 1, (size // 2) - 1]
for y in range(size):
    grid[y][0] = "|"
    grid[y][size -1] = "|"
    grid[0][y] = "-"
    grid[size - 1][y] = "-"
    grid[size - 1][0] = "-"

while game_state == "wining":
    if len(current_places) // 2 > length - 1:
        tail_x = current_places.pop(0)
        tail_y = current_places.pop(0)
        grid[tail_y][tail_x] = " "

    start_time = time.perf_counter()
    key = get_key(speed)
    if key == '\x1b[A' and move != "down":
        move_snake(current_places[-2], current_places[-1], "up", grid, current_places)
        move = "up"
    elif key == '\x1b[B' and move != "up":
        move_snake(current_places[-2], current_places[-1], "down", grid, current_places)
        move = "down"
    elif key == '\x1b[D' and move != "right":
        move_snake(current_places[-2], current_places[-1], "left", grid, current_places)
        move = "left"
    elif key == '\x1b[C' and move != "left":
        move_snake(current_places[-2], current_places[-1], "right", grid, current_places)
        move = "right"
    elif move != "non":
        move_snake(current_places[-2], current_places[-1], move, grid, current_places)

    end_time = time.perf_counter()
    if end_time - start_time < speed:
        time.sleep(speed - (end_time - start_time))
    
    os.system('cls' if os.name == 'nt' else 'clear')

    for row in grid:
        #print the grid
        print(" ".join(row))

    if current_places[-1] == 0 or current_places[-2] == 0 or current_places[-1] == size - 1 or current_places[-2] == size - 1:
        game_state = "loss"
    
    points_seen = set()
    for i in range(0, len(current_places), 2):
        point = (current_places[i], current_places[i + 1])
        if point in points_seen:
            grid[current_places[i + 1]][current_places[i]] = "X"
            game_state = "loss"
            break
        points_seen.add(point)

os.system('cls' if os.name == 'nt' else 'clear')

for row in grid:
    #print the grid
    print(" ".join(row))

print("Game over")