#import things
import itertools
import os

#def things
def numbers_that_long(n):
    #make a list
    numbers = list(range(n))

    #make the perutations
    new_list = list(itertools.product(numbers, repeat=n))

    #return the list
    return new_list

def check_for_solutions(l):
    #make your right list
    things_that_work = []

    #do it for all the perumtions
    for items in l:
        #get is lenth
        lenth = len(items)
        times_shown = [0] * lenth

        #count how many time a number is shown
        for numbers in items:
            times_shown[numbers] += 1

        #check if the two values = each other
        works = True
        for i in range(lenth):
            if times_shown[i] != items[i]:
                works = False
                break
        
        #if it works add it
        if works:
            things_that_work.append(items)
    
    #return that list
    return things_that_work

#clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

#welcome the user
base_number = int(input(f"Please put in a number and I will tell you a autobiographical number that long: "))

#get the permutations
permutations = numbers_that_long(base_number)

#check for solutions
good_list = check_for_solutions(permutations)

#clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

#if there are solutions print them
if len(good_list) > 1:
    print(f"The autobiographical numbers with a lenth of {base_number} are:")
    for number in good_list:
        print(" ".join(map(str, number)))

#remove the s if not need
elif len(good_list) > 0:
    print(f"The autobiographical number with a lenth of {base_number} is:")
    for number in good_list:
        print(" ".join(map(str, number)))

else:
    print(f"Sorry there are no autobiographical numbers with a lenth of {base_number}")