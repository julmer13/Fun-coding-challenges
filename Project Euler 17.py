#import things
import os

#def things
def letter_count(number):
    if number == 1000:
        return 11
    count = 0
    for i in range(1, len(str(number)) + 1, 1):
        if i == 1:
            number_to_test = int(str(number)[len(str(number))])
            if number_to_test in [1, 2, 6]:
                count += 3
            elif number_to_test in [4, 5, 9]:
                count += 4
            else:
                count += 5
        elif