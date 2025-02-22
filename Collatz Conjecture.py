#import things
import os

#def things
def odd_or_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
def colorize(text, color):
    colors = {
        "green": "\033[32m",
        "red": "\033[31m",
        "blue": "\033[36m",  
        "reset": "\033[0m",
    }
    return f"{colors[color]}{text}{colors['reset']}"
    
#welcome user 
os.system('cls' if os.name == 'nt' else 'clear')
starting_number = int(input(f"Input any number and I will get it down to one using the Collatz Conjecture: "))
list_of_numbers = []
current_number = starting_number
while current_number != 1:
    if odd_or_even(current_number):
        list_of_numbers.append(colorize(str(int(current_number)), "red") + colorize(" / 2 ", "blue"))
        current_number /= 2
    else:
        list_of_numbers.append(colorize(str(int(current_number)), "red") + colorize(" * 3 + 1 ", "green"))
        current_number = (current_number * 3) + 1

list_of_numbers.append(str(int(current_number)))
os.system('cls' if os.name == 'nt' else 'clear')
print(f"To get {starting_number} to one the steps are\n{' ->  '.join(list_of_numbers)}\n In all it takes {len(list_of_numbers)} steps to get {starting_number} to 1")

#fun number:29465936582356458354583648637465443212345689976453453423453564564677889876766544322098765456789734545334