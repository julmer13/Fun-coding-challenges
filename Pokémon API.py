#import things
from colorama import Fore, Style, Back, init
import json

#Get the file I need
with open("Pokémon_character_stats.json", "r", encoding="utf-8") as f:
    pokemon_data = json.load(f)

for pokemon in pokemon_data:
    pokemon["name"] = str(pokemon["name"]).capitalize()

#def things
def clear_screen():
    print("\033c", end="")

def change_av_to_full(value):
    picks = {
        "n": "name",
        "t": "types",
        "hp": "hp",
        "a": "attack",
        "he": "height",
        "w": "weight"
    }
    return picks[value.lower()]

def options(view):
    if view == "page":
        return f"""Enter one of the following:\n
S to search the Pokédex.\n
N to go to the next page.\n
P to go to the previous page.\n
Ctrl + C to end the program.\n"""
    elif view == "battle card":
        return f"""Enter one of the following:\n
S to keep searching.\n
P to go back to page view.\n
Ctrl + C to end the program.\n"""
    elif view == "searcher":
        return f"""Pick what you want to search by:\n
N to search by name\n
T to search by type\n
HP to search by HP value\n
A to search by attack value\n
He to search by height value\n
W to search by weight value\n"""

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
            if value.lower() in str(pokemon["name"]).lower():
                make_battle_card(pokemon)
                print("\n")
                items_found += 1
        print(f"Found {items_found} instance of pokémon with {value} as / in their {type}.\n")
        return None
    else:
        print("Invalid search type")
        return None
    print(f"Found {items_found} instance of pokémon with {value} as their {type}.\n")

def page_view(page_number):
    page_card = [
        [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
    ]
    offset_index = (page_number - 1) * 32
    if page_number != (len(pokemon_data) // 32) + 1:
        for p in range(1, 17):
            for i in range(len(str(pokemon_data[p + offset_index]["name"]))):
                page_card[p].append(color_text(pokemon_data[p + offset_index]["color"], str(pokemon_data[p + offset_index]["name"])[i]))
    else:
        for p in range(1, (len(pokemon_data) % 32)):
            for i in range(len(str(pokemon_data[p + offset_index]["name"]))):
                page_card[p].append(color_text(pokemon_data[p + offset_index]["color"], str(pokemon_data[p + offset_index]["name"])[i]))
    
    max_length = 0
    for p in pokemon_data:
        if len(p["name"]) > max_length:
            max_length = len(p["name"])

    for line in page_card:
        while len(line) < max_length + 3:
            line.append(" ")

    offset_index += 16
    if page_number != (len(pokemon_data) // 32) + 1:
        for p in range(1, 17):
            for i in range(len(str(pokemon_data[p + offset_index]["name"]))):
                page_card[p].append(color_text(pokemon_data[p + offset_index]["color"], str(pokemon_data[p + offset_index]["name"])[i]))
    else:
        if (len(pokemon_data) % 32) - 16 >= 1:
            for p in range(1, (len(pokemon_data) % 32)):
                for i in range(len(str(pokemon_data[p + offset_index]["name"]))):
                    page_card[p].append(color_text(pokemon_data[p + offset_index]["color"], str(pokemon_data[p + offset_index]["name"])[i]))

    for line in page_card:
        while len(line) < (max_length * 2) + 3:
            line.append(" ")

    what_to_show = str(((len(pokemon_data) // 32) + 1))[::-1] + "/"
    for l in range(len(what_to_show)):
        page_card[0][len(page_card[0]) - (1 + l)] = what_to_show[l]
    if len(str(page_number)) == 2:
        for number in range(len(str(page_number)) - 1, -1, -1):
            page_card[0][len(page_card[0]) - (len(what_to_show) + 1 + number)] = str(page_number)[1 - number]
    else:
        page_card[0][len(page_card[0]) - (len(what_to_show) + 1)] = str(page_number)

    page_card.insert(1, list(" " for _ in range((max_length * 2) + 3)))

    if page_number != (len(pokemon_data) // 32) + 1:
        what_to_show = str((page_number) * 32)[::-1] + "-"
    else:
        what_to_show = str((((page_number - 1) * 32)) + (len(pokemon_data) % 32))[::-1] + "-"
    for l in range(len(what_to_show)):
        page_card[1][len(page_card[1]) - (1 + l)] = what_to_show[l]
    offset = len(what_to_show)
    what_to_show = str(((page_number - 1) * 32) + 1)[::-1]
    for l in range(len(what_to_show)):
        page_card[1][len(page_card[1]) - (offset + 1 + l)] = what_to_show[l]
    offset += len(what_to_show)
    what_to_show = str("showing: ")[::-1]
    for l in range(len(what_to_show)):
        page_card[1][len(page_card[1]) - (offset + 1 + l)] = what_to_show[l]

    page_card.append(list(" " for _ in range((max_length * 2) + 6)))
    page_card.append(list(highlight_text("white", " ") for _ in range((max_length * 2) + 6)))

    page_card.insert(0, list(highlight_text("white", " ") for _ in range((max_length * 2) + 6)))

    for lists in range(len(page_card)):
        if lists <= 18 and lists >= 1:
            page_card[lists].insert(0, "   ")
        page_card[lists].insert(0, highlight_text("white", "  "))
        page_card[lists].append(highlight_text("white", "  "))
    
    for line in page_card:
        print("".join(line))

#main program
clear_screen()
print(f"Welcome to Pokédex\n")
welcome = True
valid = True
page_number = 1
view = "page"
try:
    while True:
        if view == "page":
            if not welcome:
                clear_screen()
            page_view(page_number)
        if not valid:
            clear_screen()
            print(f"Invalid responce try again.\n")
            view = "page"
            page_view(page_number)
        print(options(view))
        choice = input(f"Please choose one: ")
        valid = True
        if view == "page":
            if choice.lower() == "n":
                page_number += 1
                if page_number == (len(pokemon_data) // 32) + 2:
                    page_number = 1
                elif page_number == 0:
                    page_number = (len(pokemon_data) // 32) + 1
                clear_screen()
            elif choice.lower() == "p":
                page_number -= 1
                if page_number == (len(pokemon_data) // 32) + 2:
                    page_number = 1
                elif page_number == 0:
                    page_number = (len(pokemon_data) // 32) + 1
                clear_screen()
            elif choice.lower() == "s":
                clear_screen()
                page_view(page_number)
                print(options("searcher"))
                view = "battle card"
                search_type = input(f"What do you want to search by: ")
                if search_type.lower() in ["n", "t", "hp", "a", "he", "w"]:
                    search_type = change_av_to_full(search_type)
                    if search_type != "name" and search_type != "types":
                        search_value = int(input(f"What do you want {search_type} to be: "))
                    elif search_type == "name":
                        search_value = input(f"What to you want the name to be / contain: ")
                    else:
                        search_value = input(f"What type are are you searching for: ")
                    clear_screen()
                    searcher(search_type, search_value)
                else:
                    valid = False
            else:
                valid = False
        elif view == "battle card":
            if choice.lower() == "p":
                view = "page"
            elif choice.lower() == "s":
                clear_screen()
                print(options("searcher"))
                view = "battle card"
                search_type = input(f"What do you want to search by: ")
                if search_type.lower() in ["n", "t", "hp", "a", "he", "w"]:
                    search_type = change_av_to_full(search_type)
                    if search_type != "name" and search_type != "types":
                        search_value = int(input(f"What do you want {search_type} to be: "))
                    elif search_type == "name":
                        search_value = input(f"What to you want the name to be / contain: ")
                    else:
                        search_value = input(f"What type are are you searching for: ")
                    clear_screen()
                    searcher(search_type, search_value)
                else:
                    valid = False
            else:
                valid = False
        welcome = False
except KeyboardInterrupt:
    clear_screen()
    print("Good bye!")