#import things
import os

#def things
def largest_number_in_group(number, length_of_number):
    largest_number = 0
    number = str(number)
    for s in range(0, (len(number) - length_of_number) + 1, 1):
        test_number = 1
        for t in range(0, length_of_number):
            test_number *= int(number[s + t])
            if test_number > largest_number:
                largest_number = test_number
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"The largest product of {length_of_number} digits in this number is {largest_number}")

os.system('cls' if os.name == 'nt' else 'clear')

largest_number_in_group(int(input(f"Give the number: ")), int(input(f"Give me how many number in arow you want: ")))