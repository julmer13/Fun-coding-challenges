#import things
from colorama import Fore, Style, init
import json

#Get the file I need
with open("Pokémon_character_stats.json", "r", encoding="utf-8") as f:
    pokemon_data = json.load(f)


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

for pokemon in pokemon_data:
    if pokemon["name"] == "pikachu":
        print(color_text(pokemon["color"], pokemon["name"]))