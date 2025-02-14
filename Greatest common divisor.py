#import things
import math

#def things
def find_GCD(a, b):
    first_number = int(a)
    second_number = int(b)
    first_list = []
    second_list = []
    for i in range(1, math.ceil(math.sqrt(first_number)) + 1):
        if first_number % i == 0:
            first_list.append(i)
            first_list.append(first_number / i)
    print(first_list)
    for i in range(1, math.ceil(math.sqrt(second_number)) + 1):
        if second_number % i == 0:
            second_list.append(i)
            second_list.append(second_number / i)
    print(second_list)
    for number in range(len(first_list) - 1, 0, -1):
        for ints in range(len(second_list) - 1, 0, -1):
            if number == ints:
                return number

print(find_GCD(5, 20))

