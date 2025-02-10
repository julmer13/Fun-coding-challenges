#import things
import time

#def things
def move_snake(curent_place_x, curent_place_y, direction, grid, places):
    if direction == "up":
        grid[curent_place_y][curent_place_x - 1] = "# "
        places.append(curent_place_x - 1)
        places.append(curent_place_y)
    if direction == "down":
        grid[curent_place_y][curent_place_x + 1] = "# "
        places.append(curent_place_x + 1)
        places.append(curent_place_y)
    if direction == "left":
        grid[curent_place_y - 1][curent_place_x] = "# "
        places.append(curent_place_x)
        places.append(curent_place_y - 1)
    if direction == "right":
        grid[curent_place_y + 1][curent_place_x] = "# "
        places.append(curent_place_x)
        places.append(curent_place_y + 1)

grid = [[" " for _ in range(10)] for _ in range(10)]
grid[5][4] = "# "
current_places = [4, 5]
for row in grid:
    #print the grid
    print(row)
f = 4

