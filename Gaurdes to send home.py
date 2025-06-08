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
                print(f"{number_list[str(guard + 1)].capitalize()} guard going home is: {name}")
            person_going_home = name_list[random.randint(0, len(name_list) - 1)]
            print(f"{number_list[str(person + 1)].capitalize()} guard going home is: {name_list[random.randint(0, len(name_list) - 1)]}")
            time.sleep(0.03)
        guards_going_home.append(pick_random(name_list))
    return guards_going_home

clear_screen()
print("Give me the names of the guards one by one then tpye the amout of times you want there name in the list (e.g.: david 4), type done when you're done: ")
lines = [] 
while True:
    line = input()
    if line.upper() == "DONE":
        break
    line = line.split()
    for _ in range(int(line[1])):
        lines.append(line[0])
clear_screen()
number_of_people_going_home = int(input(f"How many gaurds are you sending home: "))
show_names(lines, number_of_people_going_home)