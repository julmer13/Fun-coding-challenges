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

def make_battle_card(pokemon):
    battle_card = [
        [" ", "N", "a", "m", "e", ":", " "],
        [" ", "T", "y", "p", "e", "s", ":", " "],
        [" ", "H", "P", ":", " ", " ", "A", "t", "t", "a", "c", "k", ":", " "],
        [" ", "H", "e", "i", "g", "h", "t", ":", " ", " ", "W", "e", "i", "g", "h", "t", ":" " "],
    ]
    for i in range(len(str(pokemon["name"]))):
        battle_card[0].append(color_text(pokemon["color"], str(pokemon["name"])[i]))

    for l in range(len(pokemon["types"])):
        for i in range(len(str(pokemon["types"][l]))):
            battle_card[1].append(str(pokemon["types"][l])[i])
        if l < len(pokemon["types"]) - 1:
            battle_card[1].append(",")
            battle_card[1].append(" ")

    for i in range(len(str(pokemon["hp"]))):
        battle_card[2].insert(5 + i, str(pokemon["hp"])[i])

    for i in range(len(str(pokemon["attack"]))):
        battle_card[2].append(str(pokemon["attack"])[i])

    for i in range(len(str(pokemon["height"]))):
        battle_card[3].insert(9 + i,str(pokemon["height"])[i])

    for i in range(len(str(pokemon["weight"]))):
        battle_card[3].append(str(pokemon["weight"])[i])

    for stat in battle_card:
        print("".join(stat))

for pokemon in pokemon_data:
    if pokemon["weight"] == 69:
        make_battle_card(pokemon)
        print("\n")