#import things
import os

#def things
def diffencnce_of_numbers(high_number):
    numbers_squared, number_squared = 0, 0
    for i in range(1, high_number + 1, 1):
        numbers_squared += i ** 2
        number_squared += i
    number_squared **= 2
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"The differce of the sum of the numbers under {high_number} squared and the sum of each number under {high_number} squared is {number_squared - numbers_squared}")

os.system('cls' if os.name == 'nt' else 'clear')

diffencnce_of_numbers(int(input(f"Give me a number and I will tell you he differce of the sum of the numbers under the number squared and the sum of each number under the number squared: ")))