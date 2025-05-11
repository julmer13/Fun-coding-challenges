#import things
import os

#def things
def letter_count(number:str):
    count = 0
    for i in range(1, len(number) + 1, 1):
        number_to_test = int(number[len(number) - i])
        if i == 1:
            if number_to_test in [1, 2, 6]:
                count += 3
            elif number_to_test in [4, 5, 9]:
                count += 4
            elif number_to_test != 0:
                count += 5
        elif i == 2:
            if number_to_test == 1:
                number_to_test = int(number[len(number) - 1])
                count = 0
                if number_to_test in [0]:
                    count += 3
                elif number_to_test in [1, 2]:
                    count += 6
                elif number_to_test in [5, 6]:
                    count += 7
                elif number_to_test in [7]:
                    count += 9
                else:
                    count += 8
            elif number_to_test in [7]:
                count += 7
            elif number_to_test in [4, 5, 6]:
                count += 5
            elif number_to_test != 0:
                count += 6
        elif i == 3:
            if number_to_test in [1, 2, 6]:
                count += 10
            elif number_to_test in [4, 5, 9]:
                count += 11
            elif number_to_test != 0:
                count += 12
            if int(number) % 100 != 0:
                count += 3
        elif i == 4:
            count += 11
    return count

def number_test(top_number):
    total = 0
    for n in range(1, top_number + 1):
        total += letter_count(str(n))
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"The sum of the letters in numbers 1 to {top_number} is: {total}")
os.system('cls' if os.name == 'nt' else 'clear')
number_test(int(input("Give me the top number: ")))