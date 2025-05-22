#import things
import time
import sys
import tty
import termios
import select
import shutil
import random

print("\033c", end="")
grid_spaces = "  "
other_spaces = "  "
join_space = ""
high_score = 0
grided = input("do you want a grid on the screen y/n: ")
if grided == "y":
    grid_spaces = "__"
    other_spaces = "  "
    join_space = "|"

#def things
def move_snake(curent_place_x, curent_place_y, direction, grid, places):
    if direction == "up":
        grid[curent_place_y - 1][curent_place_x] = make_colors(other_spaces, "green")
        places.append(curent_place_x)
        places.append(curent_place_y - 1)
    if direction == "down":
        grid[curent_place_y + 1][curent_place_x] = make_colors(other_spaces, "green")
        places.append(curent_place_x)
        places.append(curent_place_y + 1)
    if direction == "left":
        grid[curent_place_y][curent_place_x - 1] = make_colors(other_spaces, "green")
        places.append(curent_place_x - 1)
        places.append(curent_place_y )
    if direction == "right":
        grid[curent_place_y][curent_place_x + 1] = make_colors(other_spaces, "green")
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

def make_colors(text, color):
    colors = {
        "green": "\033[42m",
        "red": "\033[41m",  
        "white":"\33[47m",
        "reset": "\033[0m",
        "grey": "\033[100m"
    }
    return f"{colors[color]}{text}{colors['reset']}"

def add_game_over(grid, size):
    grid[(size // 2) - 1][(size // 2) - 1] = grid_spaces
    grid[(size // 2) - 1][((size // 2) - 1) - 1] = "e" + (grid_spaces[0])
    grid[(size // 2) - 1][((size // 2) - 1) - 2] = "m" + (grid_spaces[0])
    grid[(size // 2) - 1][((size // 2) - 1) - 3] = "a" + (grid_spaces[0])
    grid[(size // 2) - 1][((size // 2) - 1) - 4] = "G" + (grid_spaces[0])
    grid[(size // 2) - 1][((size // 2) - 1) + 1] = "O" + (grid_spaces[0])
    grid[(size // 2) - 1][((size // 2) - 1) + 2] = "v" + (grid_spaces[0])
    grid[(size // 2) - 1][((size // 2) - 1) + 3] = "e" + (grid_spaces[0])
    grid[(size // 2) - 1][((size // 2) - 1) + 4] = "r" + (grid_spaces[0])

def get_terminal_size():
    ter_size = shutil.get_terminal_size(fallback=(80, 24)) 
    if ter_size.columns < ter_size.lines:
        return ter_size.columns
    else:
        return ter_size.lines
    
size = get_terminal_size() - 2

try:
    while True:
        move = "non"
        speed = 0.1
        length = 1
        grid = [[grid_spaces for _ in range(size)] for _ in range(size)]
        game_state = "wining"
        grid[(size // 2) - 1][(size // 2) - 1] = make_colors(other_spaces, "green")
        current_places = [(size // 2) - 1, (size // 2) - 1]
        for y in range(size):
            grid[y][0] = make_colors(other_spaces, "white")
            grid[y][size -1] = make_colors(other_spaces, "white")
            grid[0][y] = make_colors(other_spaces, "white")
            grid[size - 1][y] = make_colors(other_spaces, "white")
            grid[size - 1][0] = make_colors(other_spaces, "white")

        apple_pos_x = random.randint(1, size - 2)
        apple_pos_y = random.randint(1, size - 2)

        grid[apple_pos_y][apple_pos_x] = make_colors(other_spaces, "red")

        while game_state == "wining":
            if len(current_places) // 2 > length + 1 and length != 1:
                tail_x = current_places.pop(0)
                tail_y = current_places.pop(0)
                grid[tail_y][tail_x] = grid_spaces

            start_time = time.perf_counter()
            key = get_key(speed)
            if key == '\x1b[A' and (move != "down" or length == 1):
                move_snake(current_places[-2], current_places[-1], "up", grid, current_places)
                move = "up"
            elif key == '\x1b[B' and (move != "up" or length == 1):
                move_snake(current_places[-2], current_places[-1], "down", grid, current_places)
                move = "down"
            elif key == '\x1b[D' and (move != "right" or length == 1):
                move_snake(current_places[-2], current_places[-1], "left", grid, current_places)
                move = "left"
            elif key == '\x1b[C' and (move != "left" or length == 1):
                move_snake(current_places[-2], current_places[-1], "right", grid, current_places)
                move = "right"
            elif move != "non":
                move_snake(current_places[-2], current_places[-1], move, grid, current_places)

            if len(current_places) // 2 > length and length == 1:
                tail_x = current_places.pop(0)
                tail_y = current_places.pop(0)
                grid[tail_y][tail_x] = grid_spaces

            end_time = time.perf_counter()
            if end_time - start_time < speed:
                time.sleep(max(0, speed - (time.perf_counter() - start_time)))
            
            print("\033c", end="")

            for row in grid:
                #print the grid
                print(join_space.join(row))
            if length > 1:
                print(f"Length: {length + 2} Score: {length - 1} High score: {high_score}")
            else:
                print(f"Length: 1 score: 0 High score: {high_score}")

            if current_places[-1] == 0 or current_places[-2] == 0 or current_places[-1] == size - 1 or current_places[-2] == size - 1:
                grid[current_places[-1]][current_places[-2]] = make_colors(other_spaces, "grey")
                game_state = "loss"
            
            points_seen = set()
            for i in range(0, len(current_places), 2):
                point = (current_places[i], current_places[i + 1])
                if point in points_seen:
                    grid[current_places[i + 1]][current_places[i]] = make_colors(grid_spaces, "grey")
                    game_state = "loss"
                    break
                elif current_places[i] == apple_pos_x and current_places[i + 1] == apple_pos_y:
                    if current_places[-1] == apple_pos_y and current_places[-2]:
                        length += 1
                        if length - 1 > high_score:
                            high_score = length - 1
                    apple_pos_x = random.randint(1, size - 2)
                    apple_pos_y = random.randint(1, size - 2)
                    grid[apple_pos_y][apple_pos_x] = make_colors(other_spaces, "red")
                    grid[current_places[-1]][current_places[-2]] = make_colors(other_spaces, "green")
                points_seen.add(point) 

        print("\033c", end="")

        add_game_over(grid, size)

        for row in grid:
            #print the grid
            print(join_space.join(row))

        if length > 1:
            print(f"Length: {length + 2} Score: {length - 1} High score: {high_score}")
        else:
            print(f"Length: 1 Score: 0 High score: {high_score}")
        input(f"press enter to play again")
except KeyboardInterrupt:
    print("Game over")