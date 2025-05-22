#import things
from colorama import Fore, Style, Back, init
import json

#Get the file I need
with open("Pokémon_character_stats.json", "r", encoding="utf-8") as f:
    pokemon_data = json.load(f)


#def things
def clear_screen():
    print("\033c", end="")

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

def highlight_text(color, text):
    highlight_map = {
    "red": Back.RED,
    "blue": Back.BLUE,
    "green": Back.GREEN,
    "yellow": Back.YELLOW,
    "brown": Back.YELLOW,
    "purple": Back.MAGENTA,
    "pink": Back.MAGENTA,
    "black": Back.BLACK,
    "white": Back.WHITE,
    "gray": Back.LIGHTBLACK_EX
}
    color_code = highlight_map.get(color.lower(), Fore.RESET)
    return(f"{color_code}{text}{Style.RESET_ALL}")

def make_battle_card(pokemon):
    battle_card = [
        [" ", "N", "a", "m", "e", ":", " "],
        [" ", "T", "y", "p", "e", "(", "s", ")", ":", " "],
        [" ", "H", "P", ":", " ", " ", "A", "t", "t", "a", "c", "k", ":", " "],
        [" ", "H", "e", "i", "g", "h", "t", ":", " ", " ", "W", "e", "i", "g", "h", "t", ":" " "],
    ]
    for i in range(len(str(pokemon["name"]))):
        battle_card[0].append(color_text(pokemon["color"], str(pokemon["name"])[i]))

    for l in range(len(pokemon["types"])):
        for i in range(len(str(pokemon["types"][l]))):
            battle_card[1].append(color_text(pokemon["color"], str(pokemon["types"][l])[i]))
        if l < len(pokemon["types"]) - 1:
            battle_card[1].append(",")
            battle_card[1].append(" ")

    for i in range(len(str(pokemon["hp"]))):
        battle_card[2].insert(5 + i, color_text(pokemon["color"], str(pokemon["hp"])[i]))

    for i in range(len(str(pokemon["attack"]))):
        battle_card[2].append(color_text(pokemon["color"], str(pokemon["attack"])[i]))

    for i in range(len(str(pokemon["height"]))):
        battle_card[3].insert(9 + i, color_text(pokemon["color"], str(pokemon["height"])[i]))

    for i in range(len(str(pokemon["weight"]))):
        battle_card[3].append(color_text(pokemon["color"], str(pokemon["weight"])[i]))

    max_length = max(len(battle_card[0]), len(battle_card[1]), len(battle_card[2]), len(battle_card[3]))

    for lists in battle_card:
        while len(lists) < max_length + 2:
            lists.append(" ")

    battle_card.append(list(" " for _ in range(max_length + 2)))
    battle_card.append(list(highlight_text(pokemon["color"], " ") for _ in range(max_length + 2)))

    battle_card.insert(0, list(" " for _ in range(max_length)))
    battle_card.insert(0, list(highlight_text(pokemon["color"], " ") for _ in range(max_length + 2)))

    for lists in battle_card:
        lists.insert(0, highlight_text(pokemon["color"], "  "))
        lists.append(highlight_text(pokemon["color"], "  "))

    battle_card[1].insert(len(battle_card[2]) // 2, "  ")
    battle_card[5].pop(len(battle_card[5]) - 2)    

    for stat in battle_card:
        print("".join(stat))

def searcher(type, value):
    items_found = 0
    if type != "name" and type != "types":
        for pokemon in pokemon_data:
            if pokemon[type] == value:
                make_battle_card(pokemon)
                print("\n")
                items_found += 1
    elif type == "types":
        for pokemon in pokemon_data:
            for types in pokemon["types"]:
                if types == value:
                    make_battle_card(pokemon)
                    print("\n")
                    items_found += 1
    elif type == "name":
        for pokemon in pokemon_data:
            if value.lower() in pokemon["name"]:
                make_battle_card(pokemon)
                print("\n")
                items_found += 1
        print(f"found {items_found} instance of pokémon with {value} in their {type}.")
        return None
    else:
        print("invalid search type")
        return None
    print(f"found {items_found} instance of pokémon with {value} as their {type}.")

clear_screen()
for pokemon in range(int(input(f"Top number: "))):
    make_battle_card(pokemon_data[pokemon])