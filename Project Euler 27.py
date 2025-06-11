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

def consecutive_primes(a, b):
    n = 0
    consecutive_primes_count = 0
    while is_prime((n ** 2) + (a * n) + (b)):
        consecutive_primes_count += 1
        n += 1
    return consecutive_primes_count

def number_test(top_value):
    longest_set_of_consecutive_primes = 0
    best_a = 0
    best_b = 0
    for A  in range(-top_value + 1, top_value):
        for B in range(2, top_value + 1, 1):
            chain = consecutive_primes(A, B)
            if chain >= longest_set_of_consecutive_primes:
                best_a = A
                best_b = B
                longest_set_of_consecutive_primes = chain
    return [best_a, best_b, best_a * best_b]
print("\033c", end="")
top_value = int(input(f"Give me the top/bottom value for this test: "))
number_list = number_test(top_value)
print("\033c", end="")
print(f"The numbers are {number_list[0]} and {number_list[1]}, they give the product of: {number_list[2]}")