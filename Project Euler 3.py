#import things 
import os
import math

#def things
def is_prime(n):
    if n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False
    if n <= 3:
        return True
    for i in range(5, math.ceil(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def Largest_Prime_Factor(number):
    largest_number = 0
    if is_prime(number):
        return number
    else:
        for i in range(math.ceil(math.sqrt(number)) + 1, 2, -1):
            if number % i == 0: 
                if is_prime(i) and i > largest_number:
                    largest_number = i
                elif number % (number / i) and i > largest_number:
                    largest_number = i

    return largest_number

os.system('cls' if os.name == 'nt' else 'clear')

print(Largest_Prime_Factor(int(input('Give me a number and I will give the largest prime factor of that number: '))))