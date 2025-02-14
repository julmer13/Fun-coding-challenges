#import things
import math

#def things
def find_GCD(a, b):
    first_number = int(a)
    second_number = int(b)
    first_list = []
    second_list = []
    for i in range(1, math.ceil(math.sqrt(first_number)) + 1):
        if first_number % i == 0:
            first_list.append(i)
            first_list.append(first_number / i)
    for i in range(1, math.ceil(math.sqrt(second_number)) + 1):
        if second_number % i == 0:
            second_list.append(i)
            second_list.append(second_number / i)
    for number in range(len(first_list) - 1, 0, -1):
        for ints in range(len(second_list) - 1, 0, -1):
            if first_list[number] == second_list[ints]:
                return first_list[number]

two_numbers = input(f"Give me to numbers and I will tell you there greatest common divisor: ").split()
print(f"The greatest common divisor of {two_numbers[0]} and {two_numbers[1]} is: {int(find_GCD(two_numbers[0], two_numbers[1]))}")

