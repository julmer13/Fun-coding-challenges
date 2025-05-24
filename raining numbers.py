#import things
import shutil
import random
import time
import math

#clear the screen
print("\033c", end="")

#def things
def get_terminal_size():
    size = shutil.get_terminal_size(fallback=(80, 24)) 
    return size.columns, size.lines

# Function to colorize a charter
def colorize(text):
    colors = {
        "reset": "\033[0m",
    }
    color = random.randint(30, 37)

    return f"\033[{color}m{text}{colors['reset']}"

#get the height and width
width, height = get_terminal_size()

#the list of all the characters
keyboard_characters = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "{", "}", "|", "[", "]", "\\", ":", ";", "\"", "'", "<", ">", ",", ".", "?", "/", "~", "`", " "
]

#get the character they want to print
speed = int(input("How fast do you want the charaters to fall: "))
speed = speed / 100

#set the x and y value
y = 0
x = random.randint(0, width - 1)

#track the numbers in the grid
falling_numbers = []

try:
    while True:
        #clear the screen
        print("\033c", end="")

        #make grid
        grid = [[" " for _ in range(width)] for _ in range(height)]
        
        #do this 50% of the time
        if random.random() < 0.375:

            #make this many charaters
            for i in range(1, random.randint(2, int(math.sqrt(width)))):
                
                #creat and store that charaters
                new_number = colorize(random.choice(keyboard_characters)) 
                x = random.randint(0, width - 1) 
                falling_numbers.append({"number": new_number, "x": x, "y": 0})
        
        #place the number on the grind and change its y value
        for number in falling_numbers:
            grid[number["y"]][number["x"]] = number["number"]
            number["y"] += 1

        falling_numbers = [num for num in falling_numbers if num["y"] < height]


        for row in grid:
            print("".join(row))

        time.sleep(speed)

except KeyboardInterrupt:
    print("\nProgram ended.")