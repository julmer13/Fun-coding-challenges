#import things
import os

#def things
def simplest_radical_form(number, tiny_number):
    outside_number = ""
    inside_number = number

    for i in range(number, 2, -1):
        if number % i == 0 and (i ** (1 / tiny_number)) % 1 == 0:
            outside_number = int(i ** (1 / tiny_number))
            inside_number = int(number / i)
            break
    new_numbers = [outside_number, inside_number]
    return new_numbers

os.system('cls' if os.name == 'nt' else 'clear')

input_numbers = (input(f"Give me the inside number and the outside number split by a space: ")).split(" ")

new_numbers = simplest_radical_form(int(input_numbers[0]), int(input_numbers[1]))

os.system('cls' if os.name == 'nt' else 'clear')

print(f"√{int(input_numbers[0])} simplifies to {new_numbers[0]}√{new_numbers[1]}")
