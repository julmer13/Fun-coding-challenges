#import things
import math
import os

#clear the screen  
os.system('cls' if os.name == 'nt' else 'clear')

#welcome the player:
numbers = input(f"Welcome to Number Game Solver. \n\nTo start think of a number and Make a range for me to guess in. \n\nFirst put in the lowest number possible than the hightest number it can be (please split them with a space): ")

#split the numbers
new_numbers = numbers.split()
for i in range(0, 2):
    new_numbers[i] = int(new_numbers[i])

#tell the user what is going to happen
input(f"\nI will now pick a number between {new_numbers[0]} and {new_numbers[1]}. If it is less than the number you are thinking of put more. If it is greater than the number that you are thinking of put less. If I guess the number you are thinking of put correct.")

#find the max number of guesses it will take
guesses = math.ceil(math.log2(new_numbers[1] - new_numbers[0] + 1))
used_guesses = 0

print(f"\nI bet I can guess your number in less than {guesses} guesses.")

#make a list of possible numbers to try
possible_numbers = []

for i in range(new_numbers[0], new_numbers[1] + 1):
    possible_numbers.append(i)

#number for later to round based on this number
base_middle_Number = math.ceil(sum(possible_numbers) / (len(possible_numbers) + 1))

#repeat this ontil you find the number
while len(possible_numbers) > 1:

    #get middle number
    middle_number = possible_numbers[len(possible_numbers) // 2]

    #make it a whole number
    if middle_number != base_middle_Number and middle_number % 1 != 0:
        if middle_number < base_middle_Number:
            middle_number = math.floor(middle_number)
        else:
            middle_number = math.ceil(middle_number)

    #ask the user
    new_input = input(f"\nIs it {int(middle_number)}: ")

    #clear the list
    possible_numbers = [
    number for number in possible_numbers
    if (new_input.lower() == "less" and number < middle_number)
    or (new_input.lower() == "more" and number > middle_number)
    or (new_input.lower() == "correct" and number == middle_number)
    ]

    #add a guess
    used_guesses += 1

if len(possible_numbers) == 0:
    print(f"You either cheated or made a mistake in putting in words")

else:
    print(f"The number you are thinking about is {possible_numbers[0]}. It took me less than {guesses} guesses, it only took me {used_guesses} guesses.")