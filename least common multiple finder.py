#import things
import os

#def things
def find_LCM(a, b):
    first_number = int(a)
    second_number = int(b)
    if first_number < second_number:
        i = 2
        while ((first_number * i) % second_number) != 0:
            i += 1
        return (first_number * i)
    
    else:
        i = 2
        while second_number * i % first_number != 0:
            i += 1
        return (second_number * i)
    
#get the numbers and clear screen
os.system('cls' if os.name == 'nt' else 'clear')
numbers = input(f"Input two number and I will tell you there least common multiple: ").split()
os.system('cls' if os.name == 'nt' else 'clear')
print(f"The least common multiple of {numbers[0]} and {numbers[1]}: {find_LCM(numbers[0], numbers[1])}")