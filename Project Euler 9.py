#import things
import os

#def things
def special_pythagorean_triplet(top_number):
    for a in range(1, top_number):
        for b in range(1, top_number - a):
            c = top_number - (a + b)
            if a ** 2 + b ** 2 == c ** 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"The three values are A: {a}, B: {b}, C: {c}, and there product is {a*b*c}")
                return
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"There is no Pythagorean triplet that eguals {top_number}")
os.system('cls' if os.name == 'nt' else 'clear')
special_pythagorean_triplet(int(input("Give me the number that you want the be the top value: ")))