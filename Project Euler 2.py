#import things
import os 

#def things
def Even_Fibonacci_Numbers_Sum(top_value):
    first_term = 1
    second_term = 1
    sum = 0
    while first_term + second_term <= top_value:
        thrid_term = first_term + second_term
        first_term = second_term
        second_term = thrid_term
        if thrid_term % 2 == 0:
            sum += thrid_term
    return sum

os.system('cls' if os.name == 'nt' else 'clear')

print(Even_Fibonacci_Numbers_Sum(int(input('give me a number and I will give you the sum of the even fibonacci numbers under that number: '))))