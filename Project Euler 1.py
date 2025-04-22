#import things
import os

#def things
def Multiples_of_3_or_5(top_value):
    total = 0
    for i in range(1, top_value, 1):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

os.system('cls' if os.name == 'nt' else 'clear')

print(f"{Multiples_of_3_or_5(int(input('Give me a number and I will tell you the total of all the numbers that are multiples of 3 or 5: ')))}")