#import things
import os
import time

#def things
def first_wave(number_list, len_of_list):
    new_list = []
    while len(new_list) < len_of_list:
        for i in range(0, 2):
            for number in number_list:
                if len(new_list) < len_of_list:
                    if i == 1:
                        new_list.append(number * -1)
                    else:
                        new_list.append(number)
    return new_list

def next_wave(number_list):
    new_number = number_list[len(number_list)-1]
    new_list = [0]
    for i in range(0, len(number_list) - 1, 1):
        new_list.append(number_list[i])
    new_list[0] = new_number
    return new_list

#clear the screen and welcome the user
os.system('cls' if os.name == 'nt' else 'clear')
input_number = int(input(f"Give me the top/bottom value for a wave of numbers: "))

list_of_possible_numbers = []

for i in range(input_number, -1, -1):
    list_of_possible_numbers.append(input_number - i)
for i in range(1, input_number):
    list_of_possible_numbers.append(input_number - i)

fred = first_wave(list_of_possible_numbers, len(list_of_possible_numbers * 2))
print(first_wave(list_of_possible_numbers, len(list_of_possible_numbers * 2)))

while True:
    print(next_wave(fred))
    time.sleep(0.5)
    fred = next_wave(fred)
    
