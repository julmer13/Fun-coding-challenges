#import things
import math
import os

#def things
def find_all_values(number_of_sides, length_of_side, apothem, radius):
    # Case 1
    if number_of_sides == "unknown" or (length_of_side == "unknown" and apothem == "unknown" and radius == "unknown"):
        return "Not enough information to solve."

    # Case 2
    if length_of_side == "unknown" and isinstance(apothem, (int, float)) and isinstance(radius, (int, float)):
        length_of_side = 2 * radius * math.sin(math.pi / number_of_sides)

    # Case 3
    if isinstance(length_of_side, (int, float)) and apothem == "unknown" and isinstance(radius, (int, float)):
        apothem = length_of_side / (2 * math.tan(math.pi / number_of_sides))

    # Case 4
    if isinstance(length_of_side, (int, float)) and isinstance(apothem, (int, float)) and radius == "unknown":
        radius = math.sqrt((apothem ** 2) + ((length_of_side / 2) ** 2))

    # Case 5
    if isinstance(length_of_side, (int, float)) and apothem == "unknown" and radius == "unknown":
        apothem = length_of_side / (2 * math.tan(math.pi / number_of_sides))
        radius = length_of_side / (2 * math.sin(math.pi / number_of_sides))

    # Case 6
    if length_of_side == "unknown" and isinstance(apothem, (int, float)) and radius == "unknown":
        length_of_side = 2 * apothem * math.tan(math.pi / number_of_sides)
        radius = math.sqrt((apothem ** 2) + ((length_of_side / 2) ** 2))

    # Case 7
    if length_of_side == "unknown" and apothem == "unknown" and isinstance(radius, (int, float)):
        length_of_side = 2 * radius * math.sin(math.pi / number_of_sides)
        apothem = radius * math.cos(math.pi / number_of_sides)

    perimeter = number_of_sides * length_of_side
    area = 0.5 * apothem * perimeter

    return f"Length of side = {length_of_side}\nApothem = {apothem}\nRadius = {radius}\nPerimeter = {perimeter}\nArea = {area}"

os.system('cls' if os.name == 'nt' else 'clear')

input(f"This program finds the values of regular polygons.\nAnswer the next four question to the best of your abilties.\nIf you can't answer one put leavew it blank and I will solve it.\nPress enter to start.")

os.system("cls" if os.name == "nt" else "clear")

num_of_sides = input(f"How many sides does the shape have: ")
len_of_side = input(f"What is the length of the side: ")
apothem = input(f"What is the apothem of the shape: ")
radius = input(f"What is the radius of the shape: ")

os.system('cls' if os.name == 'nt' else 'clear')

if num_of_sides != "":
    num_of_sides = int(num_of_sides)
else:
    num_of_sides = "unknown"

if len_of_side != "":
    len_of_side = int(len_of_side)
else:
    len_of_side = "unknown"

if apothem != "":
    apothem = int(apothem)
else:
    apothem = "unknown"

if radius != "":
    radius = int(radius)
else:
    radius = "unknown"

print(find_all_values(num_of_sides, len_of_side, apothem, radius))