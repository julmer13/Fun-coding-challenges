#import things
import os
import math

#def things
def sum_of_divisors(number):
    sum_of_div = 1
    for i in range(2, (math.isqrt(number)) + 1):
        if number % i == 0:
            if i * i == number:
                sum_of_div += i
            else:
                sum_of_div += i + (number / i)
    return int(sum_of_div)

def make_long_list(top_value):
    tuple_list = []
    for n in range(0, top_value):
        tuple_list.append((n + 1, sum_of_divisors(n + 1)))
    return tuple_list

def sum_of_amicable_numbers(tuple_list):
    index = 0
    sum_of_numbers = 0
    while len(tuple_list) >= 1:
        if (tuple_list[index][1], tuple_list[index][0]) in tuple_list and tuple_list[index][1] != tuple_list[index][0]:
            sum_of_numbers += tuple_list[index][0] + tuple_list[index][1]
            tuple_list.remove((tuple_list[index][1], tuple_list[index][0]))
            tuple_list.remove((tuple_list[index][0], tuple_list[index][1]))
        else:
            tuple_list.remove((tuple_list[index][0], tuple_list[index][1]))
    return sum_of_numbers
os.system('cls' if os.name == 'nt' else 'clear')
top_number = int(input(f"Give the top number: "))
os.system('cls' if os.name == 'nt' else 'clear')
print(f"The sum of micable numbers under {top_number} is: {sum_of_amicable_numbers(make_long_list(top_number))}")