#import things
import os
from itertools import permutations

#def things
def different_numbers(list_of_digits, index):
    str_list = ''.join(list_of_digits)
    new_list = sorted(list(permutations(str_list)))
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"The number at index {index} is: {''.join(new_list[index - 1])}")
os.system('cls' if os.name == 'nt' else 'clear')
list_of_digits = input("Enter the list of digits separated by spaces: ").split()
index = int(input("Enter the index of the permutation: "))
different_numbers(list_of_digits, index)