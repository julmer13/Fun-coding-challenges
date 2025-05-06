#import things
import os
import math

#def things
def number_of_divisors(number):
    num_of_div = 2
    for i in range(2, (math.isqrt(number)) + 1,):
        if number % i == 0:
            if i * i == number:
                num_of_div += 1
            else:
                num_of_div += 2
    return num_of_div

def number_tester(top_number):
    number_to_add = 2
    start_number = 1
    while number_of_divisors(start_number) < top_number:
        start_number += number_to_add
        number_to_add += 1
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"The first triangle number to have over {top_number} is {start_number}")

os.system('cls' if os.name == 'nt' else 'clear')
number_tester(int(input(f"Give me a number and I will give the first triangle number to have more than that number of dividers: ")))