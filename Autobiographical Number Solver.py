#import things
import itertools
import os

#def things
def numbers_that_long(n):
    #make a list
    numbers = list(range(n))
    numbers_that_work = []

    #get the numbers need
    length = n

    #set the max number
    number = 1
    for t in range(0, n):
        number *= 10

    #go though all the numbers
    for items in range (0, number):
        #is valid
        is_valid = True
        total = 0
        times_shown = [0] * length

        #add 0 if needed
        if items < 10**(n - 1):
            item = str(items).zfill(length)
        else:
            item = items
        print(item)
        item = int(item)

        digits = []
        while item > 0:
            digits.insert(0, item % 10)
            item //= 10

        for digit in digits:
            if digit >= n - 1 and is_valid:
                is_valid = False
            
            if is_valid:
                times_shown[digit] += 1
                
                total += digit

        if total != n and is_valid:
            is_valid = False

        if is_valid:
           for i in range(length):
                if times_shown[i] != digits[i] and is_valid:
                    is_valid = False
                    break 
        
        if is_valid:
            print(item)
            numbers_that_work.append(item)
    
    return numbers_that_work


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

# #check for solutions
# good_list = check_for_solutions(permutations)

##clear the screen
#os.system('cls' if os.name == 'nt' else 'clear')

print(permutations)

# #if there are solutions print them
# if len(good_list) > 1:
#     print(f"The autobiographical numbers with a lenth of {base_number} are:")
#     for number in good_list:
#         print(" ".join(map(str, number)))

# #remove the s if not need
# elif len(good_list) > 0:
#     print(f"The autobiographical number with a lenth of {base_number} is:")
#     for number in good_list:
#         print(" ".join(map(str, number)))

# else:
#     print(f"Sorry there are no autobiographical numbers with a lenth of {base_number}")