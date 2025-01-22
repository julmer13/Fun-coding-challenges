import os

os.system('cls' if os.name == 'nt' else 'clear')

#welcome the user
user_input = input("Give me a number and I will tell you its digital root: ")

i = 10
new_number = int(user_input)
while i >= 9:
    new_i = 0
    loop_number = len(str(new_number))
    for n in range(loop_number):
        new_i += new_number % 10
        new_number //= 10

    i = new_i
    new_number = new_i

print(f"The digital root of {user_input} is {i}")