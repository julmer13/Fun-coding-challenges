#import things
from colorama import Fore, Style, Back, init

#house keeping
guess_list = []
number_to_color = {0:"r", 1:"p", 2:"g", 3:"y", 4:"w", 5:"b"}

#def things
def make_all_possible_guesses():
    for first in range(6):
        for second in range(6):
            for third in range(6):
                for fourth in range(6):
                    fake_list = [number_to_color[first], number_to_color[second], number_to_color[third], number_to_color[fourth]]
                    guess_list.append(fake_list)
def highlight_text(color, text):
    highlight_map = {
    "r": Back.RED,
    "p": Back.BLUE,
    "g": Back.GREEN,
    "y": Back.YELLOW,
    "w": Back.WHITE,
    "b": Back.BLACK,
    "grey": Back.LIGHTBLACK_EX
}
    color_code = highlight_map.get(color.lower(), Fore.RESET)
    return(f"{color_code}{text}{Style.RESET_ALL}")

def print_results(guess_list):
    for guesse in guess_list:
        new_list = []
        for color in guesse:
            new_list.append(highlight_text(color, color + " "))
        print("".join(new_list))

make_all_possible_guesses()
print_results(guess_list)