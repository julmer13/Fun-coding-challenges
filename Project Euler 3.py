#import things 
import os
import math

#def things
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def Largest_Prime_Factor(number):
    if is_prime(number) != True:
        prime_factor = 0
        for i in range(math.floor(number / 2), 1, -1):
            if number % i == 0 and is_prime(i):
                prime_factor = i
                break
        if prime_factor > 0: return prime_factor
        else: return "there is no prime factors"
    else: return number

os.system('cls' if os.name == 'nt' else 'clear')

print(Largest_Prime_Factor(int(input('Give me a number and I will give the largest prime factor of that number: '))))