#import things
import os
import math

os.system('cls' if os.name == 'nt' else 'clear')
length_of_wall = int(input(f"Give me the length of the side of the grid: "))
print(f"There are {int(math.factorial(length_of_wall * 2) / math.factorial(length_of_wall) ** 2)} unquie ways through this maze: ")