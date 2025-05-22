#import things
from colorama import Fore, Style, init

#def things
def color_text(color, text):
    color_map = {
    "red": Fore.RED,
    "blue": Fore.BLUE,
    "green": Fore.GREEN,
    "yellow": Fore.YELLOW,
    "brown": Fore.YELLOW,
    "purple": Fore.MAGENTA,
    "pink": Fore.MAGENTA,
    "black": Fore.BLACK,
    "white": Fore.WHITE,
    "gray": Fore.LIGHTBLACK_EX
}
    color_code = color_map.get(color.lower(), Fore.RESET)
    return(f"{color_code}{text}{Style.RESET_ALL}")

print(color_text("red", "red"))