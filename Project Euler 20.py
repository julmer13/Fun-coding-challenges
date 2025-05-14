import os

os.system('cls' if os.name == 'nt' else 'clear')

number = int(input(f"Tell me the number you want to get the sum of its factorial: "))

total = 1

for i in range(1, (number + 1)):
    total *= i

print_total = total

digits = []
while total > 0:
    digit = total % 10
    digits.insert(0, digit)
    total //= 10

os.system('cls' if os.name == 'nt' else 'clear')

print(f"{number} factorial is {print_total}, the sum of these digits is {sum(digits)}")