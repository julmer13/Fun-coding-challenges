#import things
from colorama import Fore, Style, Back, init

#house keeping
list_of_possible_solutions = []
number_to_color = {0:"r", 1:"p", 2:"g", 3:"y", 4:"w", 5:"b"}

#def things
def make_all_possible_guesses():
    for first in range(6):
        for second in range(6):
            for third in range(6):
                for fourth in range(6):
                    fake_list = [number_to_color[first], number_to_color[second], number_to_color[third], number_to_color[fourth]]
                    list_of_possible_solutions.append(fake_list)


def mock_run(guess, mock_answer):
    blacks = 0
    whites = 0

    test_guess = guess[:]
    test_answer = mock_answer[:]

    for color in range(4):

        if test_guess[color] == test_answer[color]:
            blacks += 1
            test_answer[color] = None
            test_guess[color] = None

    for color in range(4):

        if test_guess[color] is not None and test_guess[color] in test_answer:
            whites += 1
            test_answer[test_answer.index(test_guess[color])] = None

    return blacks, whites

def get_rid_of_impossible_answers(guess, feed_back_black, feed_back_white, list_of_possible_solutions):
    new_list = []

    for solution in list_of_possible_solutions:

        blacks, whites = mock_run(guess, solution)

        if blacks == feed_back_black and whites == feed_back_white:
            new_list.append(solution)

    return new_list
                
def highlight_text(color, text):
    highlight_map = {
    "r": Back.RED,
    "p": Back.BLUE,
    "g": Back.GREEN,
    "y": Back.YELLOW,
    "w": Back.WHITE,
    "b": Back.BLACK,
    "grey": Back.LIGHTBLACK_EX
}
    color_code = highlight_map.get(color.lower(), Fore.RESET)
    return(f"{color_code}{text}{Style.RESET_ALL}")

def print_results(guess_list):

    for guesse in guess_list:

        new_list = []

        for color in guesse:
            new_list.append(highlight_text(color, color + " "))

        print("".join(new_list))

def get_guess_and_feed_back():
    guess = list(input(f"What did you guess: "))
    feed_back = input(f"What was the feedback: ")
    blacks, whites = feed_back.count(":"), feed_back.count(".")
    return guess, blacks, whites

try:
    while True:

        make_all_possible_guesses()
        print("\033c", end="")

        while len(list_of_possible_solutions) > 1:
            guess, blacks, whites = get_guess_and_feed_back()

            list_of_possible_solutions = get_rid_of_impossible_answers(guess, blacks, whites, list_of_possible_solutions)

            print("\033c", end="")

            print_results(list_of_possible_solutions)

        print("\033c", end="")
        print("The answer was: ", end="")
        print_results(list_of_possible_solutions)
        input(f"Press enter to run the program again or Ctrl + C to end the program: ")

except KeyboardInterrupt:
    print("\033c", end="")