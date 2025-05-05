#import things
import os
import math

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

def number_tester(number_of_primes):
    primes_found = 1
    number_to_test = 3
    while primes_found < number_of_primes:
        if is_prime(number_to_test):
            primes_found += 1
        number_to_test += 1
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"The {number_of_primes} prime is {number_to_test - 1}")
    
number_tester(int(input(f"give me a number and I will give you that number prime: ")))  