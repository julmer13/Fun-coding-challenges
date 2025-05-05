#import thing
import os

#def things
def divisable_by_numbers_under(number, top_number):
    for i in range(top_number, ((top_number // 2) - (top_number % 2)), -1):
        if number % i != 0:
            return False
    return True

def Smallest_Multiple(top_number):
    test_number = top_number
    while divisable_by_numbers_under(test_number, top_number) == False:
        test_number += top_number
    print(f"The first number that is diviable by all the numbers under {top_number} is: {test_number}")

os.system('cls' if os.name == 'nt' else 'clear')

Smallest_Multiple(int(input(f"give me a number and I will tell you the first number that is divisable by all the numbers under it: ")))