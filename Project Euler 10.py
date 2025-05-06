#import things
import math
import os

#def things
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, math.ceil(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def number_tester(top_number):
    prime_number = 2
    start_number = 3
    while start_number <= top_number:
        if is_prime(start_number):
            prime_number += start_number
        start_number += 1
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"The sum of all primes under {top_number} is {prime_number}")
os.system('cls' if os.name == 'nt' else 'clear')
number_tester(int(input(f"Give me a nubmer and I will give you all the sum of all the prime numbers under it: ")))