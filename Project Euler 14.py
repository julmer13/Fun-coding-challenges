#import things
import os

#def things
def biggest_chain_collatz_conjecyure(top_number):
    longest_chain = 0
    for n in range(1, top_number, 1):
        chain = 0
        test_number = n
        print(f"test: {n}")
        while test_number != 1:
            if test_number % 2 == 0:
                test_number /= 2
            else:
                test_number = (test_number * 3) + 1
            chain += 1
        if longest_chain < chain:
            longest_chain = chain
            number_of_chain = n
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"The number under {top_number} to have the longest collatz chain is {number_of_chain} with {longest_chain} steps")

os.system('cls' if os.name == 'nt' else 'clear')
biggest_chain_collatz_conjecyure(int(input(f"Give the top value: ")))