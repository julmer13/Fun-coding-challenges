#import things
import shutil
import random
import time

#housekeeping
#make the spaces
grid_spaces = "·"
steps = "#"

#set head
head_2 = "#"

#clear screen
print("\033c", end="")

#set the speed
speed = float(input(f"Put in the speed in seconds the lowest you can go is 0.05: "))

#set beging direction
direction = random.choice(["right", "left", "up", "down"])

#make the bais
bias = int(input(f"How straight do you want it to go, 0 is no straight lines: "))

#def things
def get_terminal_size():
    #get terminal size
    ter_size = shutil.get_terminal_size(fallback=(80, 24)) 

    #return the size
    return ter_size.columns // 2, ter_size.lines - 2

#clear screen
def clear():
    print("\033c", end="")

#check a place to see if has a step there
def check_direction(direction, current_spot_x, current_spot_y):
    #get the side lengths
    x_size, y_size = get_terminal_size()

    #check right
    if direction == "right":
        if current_spot_x + 1 >= x_size or grid[current_spot_y][current_spot_x + 1] == steps:
            return False
    
    #check left
    elif direction == "left":
        if current_spot_x - 1 < 0 or grid[current_spot_y][current_spot_x - 1] == steps:
            return False
    
    #check up
    elif direction == "up":
        if current_spot_y - 1 < 0 or grid[current_spot_y - 1][current_spot_x] == steps:
            return False
    
    #check down
    elif direction == "down":
        if current_spot_y + 1 >= y_size or grid[current_spot_y + 1][current_spot_x] == steps:
            return False
    
    #if it is not a direction return false
    else:
        return False
    
    #if a if statement fails it will return true
    return True

#move character
def move_character(last_movement, current_spot_x, current_spot_y, head):
    #make list of possible movements
    places_to_move = ["right", "left", "up", "down"]

    #set the back to a step
    grid[current_spot_y][current_spot_x] = steps

    valid_places_to_move = []
    #check each place to move to
    for place in places_to_move:
        if check_direction(place, current_spot_x, current_spot_y):
            valid_places_to_move.append(place)

    #check if trapped
    if len(valid_places_to_move) == 0:
        return "trapped", current_spot_y, current_spot_x, head
    
    # Bias: favor last_movement if it's valid
    weighted_moves = []
    for d in valid_places_to_move:
        if d == last_movement:
            weighted_moves.extend([d]*bias)  # Favor straight (weight = 4)
        else:
            weighted_moves.append(d)      # Others (weight = 1)

    direction = random.choice(weighted_moves)

    #move in that direction
    #right:
    if direction == "right":
        current_spot_x += 1
        head = ">"
    
    #left:
    elif direction == "left":
        current_spot_x -= 1
        head = "<"

    #up:
    elif direction == "up":
        current_spot_y -= 1
        head = "⌃"

    #down:
    elif direction == "down":
        current_spot_y += 1
        head = "⌄"
    
    #update the grid
    grid[current_spot_y][current_spot_x] = head

    #return data
    return direction, current_spot_y, current_spot_x, head

#reset if needed:
try:
    while True:

        #start steps
        number_of_steps = 0

        #clear the screen
        print("\033c", end="")

        #set beging direction
        direction = random.choice(["right", "left", "up", "down"])

        #make grid
        x_size, y_size = get_terminal_size()
        grid = [[grid_spaces for _ in range(x_size)] for _ in range(y_size)]

        #set the end varible
        trapped = False

        #make (0,0) steps
        grid[y_size // 2][x_size // 2] = steps

        #set the staring point
        current_y, current_x = y_size // 2, x_size // 2

        #run well not trapped
        while not trapped:
            #get the start time
            start_time = time.perf_counter()

            #get the direction and current_spots
            direction, current_y, current_x, head_2 = move_character(direction, current_x, current_y, head_2)

            #check if we are trapped
            if direction == "trapped":
                trapped = True
                continue
            
            #update steps
            number_of_steps += 1

            #clear screen first
            clear()

            #print the grid
            for line in grid:
                print(" ".join(line))

            #show number_of_steps
            print(f"Number of steps taken is {number_of_steps}")

            #get end time
            end_time = time.perf_counter()

            #wait the time
            if end_time - start_time < speed:
                time.sleep(max(0, speed - (time.perf_counter() - start_time)))

        #print the end state
        grid[current_y][current_x] = head_2

        #clear the screen
        clear()

        #print the grid
        for line in grid:
            print(" ".join(line))

        #print the final step count
        print(f"In total it {speed * number_of_steps} seconds, with a total of {number_of_steps} steps.")

        #make sure the program can repeat
        input(f"Press enter to run the program again: ")

#end the program if needed
except KeyboardInterrupt:
    print("program ended")