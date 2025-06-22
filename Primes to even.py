#import things
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

def number_test(number):
    if number == 2:
        return [0, 2]
    if number == 4:
        return [2, 2]
    for d in range(3, number, 2):
        if is_prime(d) and is_prime(number - d):
            return [d, number - d]

print("\033c", end="")

try:
    while True:
        number = 1
        while number % 2 == 1: 
            number = int(input("Give me a even number and I will give you two prime numbers that make that number: "))
        
        answers = number_test(number)
        print("\033c", end="")
        print(f"To make {number} you add {answers[1]} and {answers[0]} so: {answers[1]} + {answers[0]} = {number}")

except KeyboardInterrupt:
    print("program ended", end="")