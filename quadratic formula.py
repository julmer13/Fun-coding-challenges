#import things
from fractions import Fraction
import math
import os

#def things
def solve_polynomial(a, b, c):
    #solution one
    solution_one = ((b * -1) + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)

    #solution two
    solution_two = ((b * -1) - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)

    (int(solution_one) if is_decimal(solution_one) == False else solution_one)

    return (int(solution_one) if is_decimal(solution_one) == False else solution_one), (int(solution_two) if is_decimal(solution_two) == False else solution_two)

def is_decimal(num):
    #Check if a number is a decimal.
    return isinstance(num, float) and num % 1 != 0

def convert_to_fraction(num):
    #Convert a decimal to a fraction if needed
    return Fraction(num).limit_denominator() if is_decimal(num) else num

os.system('cls' if os.name == 'nt' else 'clear') 

input_list = input(f"Give me A, B, C, split by spaces: ")
input_list = input_list.split()

solutions = solve_polynomial(float(input_list[0]), float(input_list[1]), float(input_list[2]))

os.system('cls' if os.name == 'nt' else 'clear')

input(f"x1 = {solutions[0]}\nx2 = {solutions[1]}\n\nPress enter to change the numbers into frations: ")

os.system('cls' if os.name == 'nt' else 'clear')

input(f"x1 = {convert_to_fraction(solutions[0])}\nx2 = {convert_to_fraction(solutions[1])}")