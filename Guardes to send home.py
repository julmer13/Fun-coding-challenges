#import things
import random
import time

#housekeeping
number_list = {
    "1": "first",
    "2": "second",
    "3": "thrid",
    "4": "fourth",
    "5": "fith",
    "6": "sixth",
    "7": "seventh",
    "8": "eighth",
    "9": "nineth"
}

#def things
def clear_screen():
    print("\033c", end="")

def pick_random(Names_list):
    random.shuffle(Names_list)
    poeple_to_send_home = ""
    for i in range(1):
        Name = Names_list[random.randint(0, len(Names_list) - 1)]
        poeple_to_send_home = Name
        while Name in Names_list:
            Names_list.remove(Name)
    return poeple_to_send_home

def show_names(name_list, number_of_poeple_going_home):
    guards_going_home = []
    for person in range(number_of_poeple_going_home):
        for _ in range(random.randint(30, 70)):
            clear_screen()
            for guard in range(len(guards_going_home)):
                name = guards_going_home[guard]
                print(f"The {number_list[str(guard + 1)].capitalize()} guard going home is: {name}")
            print(f"The {number_list[str(person + 1)].capitalize()} guard going home is: {name_list[random.randint(0, len(name_list) - 1)]}")
            time.sleep(0.03)
        guards_going_home.append(pick_random(name_list).capitalize())
    clear_screen()
    for guard in range(len(guards_going_home)):
        name = guards_going_home[guard]
        print(f"The {number_list[str(guard + 1)].capitalize()} guard going home is: {name}")
    return guards_going_home

clear_screen()

Base_number = 4

print(f"Give me the names of the guards one by one then tpye the amout of times you want there name in the list (e.g.: david 4),\nif you don't put in a second number it will be set to {Base_number}\ntpye done when you are done:")
lines = [] 
while True:
    line = input()
    if line.upper() == "DONE":
        break
    line = line.split()
    if len(line) >= 2:
        for _ in range(int(line[1])):
            lines.append(line[0])
    else:
        for _ in range(Base_number):
            lines.append(line[0])
clear_screen()
number_of_people_going_home = int(input(f"How many gaurds are you sending home: "))
names = show_names(lines, number_of_people_going_home)
print(f"\nThe guards going home are: {', '.join(names)}")