#import things
import os

#def things
def palindrome_tester(number):
    new_number = str(number)
    if new_number == new_number[::-1]:
        return True
    else:
        return False
    
def number_tester(number_of_digits):
    largest_palindrone = 0
    for a in range(int("9" * number_of_digits), (10 ** (number_of_digits - 1)), -1):
        for b in range(int("9" * number_of_digits), (10 ** (number_of_digits - 1)), -1):
            if palindrome_tester(a * b) and a * b > largest_palindrone:
                largest_palindrone = a * b
                digit_one = a
                digit_two = b
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"The largest palindrone that can be made with two {number_of_digits}-digit numbers is {largest_palindrone} from {digit_one} and {digit_two}")
            
os.system('cls' if os.name == 'nt' else 'clear')

number_tester(int(input(f"Give me a number of digits and I will give give you the largest palindrone that can be made with two of those digits numbers: ")))