#def things
def number_tester(top_number):
    top_repeating_value = 0
    biggest_number = 0
    for number in range(1, top_number + 1):
        value = get_repeat_value(number)
        if value >= top_repeating_value:
            top_repeating_value = value
            biggest_number = number
    return biggest_number

def get_repeat_value(number):
    fake_number = number
    while fake_number % 2 == 0:
        fake_number //= 2
    while fake_number % 5 == 0:
        fake_number //= 5
    if fake_number == 1:
        return 0
    mod_number = 1
    while pow(10, mod_number, fake_number) != 1:
        mod_number += 1
    return mod_number
print("\033c", end="")
high_number = input(f"Give me the top value: ")
print("\033c", end="")
print(f"The number to have the highest number of repeating digits below {high_number}, is {number_tester(int(high_number))}")
