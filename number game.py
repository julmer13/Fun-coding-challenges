#import things
import random
import os

#house keeping
right_answer =  random.randint(1, 100)
is_player_correct = False
trys = 0

#clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

#welcome the player
print("Welcome to the Number Guessing Game!" + "\n" + "I'm thinking of a number between 1 and 100: ")

try:
    while True:
        while is_player_correct == False:
            guess = float(input("\n" + "Enter your guess: "))
            if guess > right_answer:
                print("Too high! Try again.")

            elif guess < right_answer:
                print("Too low! Try again.")

            else:
                is_player_correct = True
            
            trys += 1

        print(f"\nCorrect! You guessed the number in {trys} attempts")

        input("Press enter to play again ")

        right_answer =  random.randint(1, 100)

        is_player_correct = False
        
        trys = 0
        #clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')

        #welcome the player
        print("Welcome to the Number Guessing Game!" + "\n" + "I'm thinking of a number between 1 and 100: ")

except KeyboardInterrupt:
    print("Game Over!")
