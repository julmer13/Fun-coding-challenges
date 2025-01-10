import os

os.system('cls' if os.name == 'nt' else 'clear')

number = int(input(f"Tell me the number you want to get the sum of its factorial: "))

total = 1

for i in range(1, (number + 1)):
    total *= i

digits = []
while total > 0:
    digit = total % 10
    digits.insert(0, digit)
    total //= 10

os.system('cls' if os.name == 'nt' else 'clear')

print(f"The sum of the digits in {number}'s factorial is {sum(digits)}")