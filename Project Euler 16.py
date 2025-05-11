#import things
import os

#def things
def sum_of_digits(number):
    number_of_digits = 0
    new_number = number
    while new_number >= 1:
        number_of_digits += new_number % 10
        new_number //= 10
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"The sum of the digits in {number} is {number_of_digits}")
os.system('cls' if os.name == 'nt' else 'clear')
sum_of_digits(int(input(f"Give the number: ")))