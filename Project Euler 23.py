#import things
import os
import math

#def things
def abundant_or_not(number):
    sum_of_div = 1
    for i in range(2, (math.isqrt(number)) + 1):
        if number % i == 0:
            if i * i == number:
                sum_of_div += i
            else:
                sum_of_div += i + (number / i)
    return sum_of_div > number

def find_all_abundant_numbers():
    list_of_abundant_numbers = []
    for number in range(1, 28124):
        if abundant_or_not(number):
            list_of_abundant_numbers.append(number)
    return list_of_abundant_numbers

def sum_of_other_numbers(all_abundant_numbers):
    abundant_numbers_sum_set = set()
    for first_index in range(0, len(all_abundant_numbers)):
        for second_index in range(first_index, len(all_abundant_numbers)):
            if all_abundant_numbers[first_index] + all_abundant_numbers[second_index] <= 28123:
                abundant_numbers_sum_set.add(all_abundant_numbers[first_index] + all_abundant_numbers[second_index])
            else:
                break
    return (28123 * (28123 + 1) // 2) - sum(abundant_numbers_sum_set)
os.system('cls' if os.name == 'nt' else 'clear')
print(sum_of_other_numbers(find_all_abundant_numbers()))