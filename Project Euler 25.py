import os

def find_number(n):
    a = 1
    b = 1
    c = 0
    digits = 0
    times = 2
    good_list = []
    if n == 0:
        return 0
    elif n == 1:
        return 1
    while digits <= n - 1:
        digits = 0
        c = a + b
        a = b
        b = c
        times += 1
        while c != 0:
            digits += 1
            c //= 10
    
    c = a + b
    good_list.append(c)
    good_list.append(times)
    return good_list 

os.system('cls' if os.name == 'nt' else 'clear')

number = int(input(f"Give me a number and I will give you that fibonacci number: "))

best_list = find_number(number)

os.system('cls' if os.name == 'nt' else 'clear')

print(f"The first fibonacci number to have {number} digits is: {best_list[0]} with a index of {best_list[1]}")

