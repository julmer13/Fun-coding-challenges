#import things
from colorama import Fore, Style, Back, init
import shutil
import math
import random

#house keeping
number_to_color = {0:"r", 1:"p", 2:"g", 3:"y", 4:"w", 5:"b", 6:"k", 7:"c"}
possible_feed_back = [[0,0],[0,1],[0,2],[0,3],[0,4],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[3,0],[3,1]]
possible_feed_back_symbols = feedbacks = ["", ".", "..", "...", "....", ":", ":.", ":..", ":...", "::", "::.", "::..", ":::", ":::.","::::"]
color_abbrs = ["r", "p", "g", "y", "w", "b", "k", "c"]
letters_on_or_off = "hi"
letters_on_or_off = None

#def things
def get_if_letters_on_or_off():
    letters_on_or_off = "on"

    while letters_on_or_off != True and letters_on_or_off != False:
        letters_on_or_off = input(f"Do you want letters with the colors: y or n: ")
        
        if letters_on_or_off.lower() == "y":
            letters_on_or_off = True

        elif letters_on_or_off.lower() == "n":
            letters_on_or_off = False

        else:
            print(f"Invald response")

    print("\033c", end="")

def get_terminal_size():
    ter_size = shutil.get_terminal_size(fallback=(80, 24)) 
    return max(1, math.floor(ter_size.columns / 10) - 1)
    
def make_all_possible_guesses():
    master_list = []
    n = len(color_abbrs)
    for first in range(n):
        for second in range(n):
            for third in range(n):
                for fourth in range(n):
                    fake_list = [number_to_color[first], number_to_color[second], number_to_color[third], number_to_color[fourth]]
                    master_list.append(fake_list)
    return master_list

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
    "k": Back.LIGHTMAGENTA_EX, 
    "c": Back.CYAN,
    "grey": Back.LIGHTBLACK_EX
}
    color_code = highlight_map.get(color.lower(), Fore.RESET)
    return(f"{color_code}{text}{Style.RESET_ALL}")

def scorer(list_of_possible_solutions):
    big_list = make_all_possible_guesses()

    best_answers = []
    best_entropy = -math.inf

    #for ties
    best_worst_bucket = math.inf

    len_of_list = len(list_of_possible_solutions)

    if len_of_list == 0:
        return [], math.inf

    for solution in big_list:
            count = {}

            for solution2 in list_of_possible_solutions:
                #use b for black and w for white. this is ading how likely somthing is going to happen
                b, w = mock_run(solution, solution2)
                #add 1 to that feedback in the dictionary
                count[(b, w)] = count.get((b, w), 0) + 1

            #e is the entropy value and starts as nothing
            E = 0.0
            #∑ = stands for a range
            for feed_backs in count.values():
                #get the probaility using the number of that feedback / by the total len of the list
                probability = feed_backs / len_of_list
                #use log to more evenly spread the probability out
                E -= probability * math.log2(probability)

            total = max(count.values())

            if E > best_entropy:
                best_entropy = E
                best_worst_bucket = total
                best_answers = [solution]

            elif E == best_entropy:
                if total < best_worst_bucket:
                    best_worst_bucket = total
                    best_answers = [solution]
                elif total == best_worst_bucket:
                    best_answers.append(solution)

    return best_answers, best_entropy

def get_guess_and_feed_back():
    guess = list(input(f"What did you guess: "))

    big_list = make_all_possible_guesses()
    while guess not in big_list:
        print("Invalid guess")
        guess = list(input(f"What did you guess: "))

    feed_back = input(f"What was the feedback: ")

    while feed_back not in possible_feed_back_symbols:
        print("Invalid feedback")
        feed_back = input(f"What was the feedback: ")

    blacks, whites = feed_back.count(":"), feed_back.count(".")
    return guess, blacks, whites

def print_sugggested_quess(guess, score):
    print(f"The guesses' entropy score: {score}")

    master_list = []
    ter_size = get_terminal_size()
    
    for y in range(math.ceil(len(guess) / ter_size)):

        master_list.append([])

        for x in range(ter_size):

            if ((y*ter_size) + x) <= len(guess) -1:
            
                master_list[y].append(highlight_text("grey", "  "))

                for z in range(4):
                    if letters_on_or_off:
                        master_list[y].append(highlight_text(guess[(y*ter_size) + x][z], guess[(y*ter_size) + x][z] + " "))

                    else:
                        master_list[y].append(highlight_text(guess[(y*ter_size) + x][z], "  "))

        if y != len(guess) // ter_size and ((y*ter_size) + x) <= len(guess) -1: 
            master_list[y].append(highlight_text("grey", "  "))
 
    while len(master_list[-1]) != (ter_size * 5) + 1:
        master_list[y].append(highlight_text("grey", "  "))

    for _ in range((ter_size * 5) + 1):
        print(highlight_text("grey", "  "), end="")
    print(f"\n", end="")

    for line in master_list:

        print("".join(line))

        for _ in range((ter_size * 5) + 1):
            print(highlight_text("grey", "  "), end="")
        print(f"\n", end="")
    
    print(end=f"\n")
        
    printed_list = [[],[],[]]

    guess = [random.choice(guess)]

    for _ in range(6):
        printed_list[0].append(highlight_text("grey", "  "))
    
    if letters_on_or_off:
        printed_list[1] = [highlight_text("grey", "  "), highlight_text(guess[0][0], guess[0][0] + " "), highlight_text(guess[0][1], guess[0][1] + " "), highlight_text(guess[0][2], guess[0][2] + " "), highlight_text(guess[0][3], guess[0][3] + " "), highlight_text("grey", "  ")]

    else:
        printed_list[1] = [highlight_text("grey", "  "), highlight_text(guess[0][0], "  "), highlight_text(guess[0][1], "  "), highlight_text(guess[0][2], "  "), highlight_text(guess[0][3], "  "), highlight_text("grey", "  ")]

    for _ in range(6):
        printed_list[2].append(highlight_text("grey", "  "))

    for row in range(len(printed_list)):

        if row in [0, 2]:
            print("                ", end="")
        else:
            print("possible guess: ", end="")

        print("".join(printed_list[row]))

    print(end=f"\n")

def print_remaining_guess(list_of_possible_solutions):
    print(f"Remaining solutions: {len(list_of_possible_solutions)}/{len(color_abbrs)**4}: ")
    
    master_list = []
    ter_size = get_terminal_size()
    
    for y in range(math.ceil(len(list_of_possible_solutions) / ter_size)):

        master_list.append([])

        for x in range(ter_size):

            if ((y*ter_size) + x) <= len(list_of_possible_solutions) -1:
            
                master_list[y].append(highlight_text("grey", "  "))

                for z in range(4):
                    if letters_on_or_off:
                        master_list[y].append(highlight_text(list_of_possible_solutions[(y*ter_size) + x][z], list_of_possible_solutions[(y*ter_size) + x][z] + " "))

                    else:
                        master_list[y].append(highlight_text(list_of_possible_solutions[(y*ter_size) + x][z], "  "))

        if y != len(list_of_possible_solutions) // ter_size and ((y*ter_size) + x) <= len(list_of_possible_solutions) -1: 
            master_list[y].append(highlight_text("grey", "  "))
 
    while len(master_list[-1]) != (ter_size * 5) + 1:
        master_list[y].append(highlight_text("grey", "  "))

    for _ in range((ter_size * 5) + 1):
        print(highlight_text("grey", "  "), end="")
    print(f"\n", end="")

    for line in master_list:

        print("".join(line))

        for _ in range((ter_size * 5) + 1):
            print(highlight_text("grey", "  "), end="")
        print(f"\n", end="")
    
    print(end=f"\n")

def print_answer(guess):
    printed_list = [[],[],[]]

    for _ in range(6):
        printed_list[0].append(highlight_text("grey", "  "))
    
    if letters_on_or_off:
        printed_list[1] = [highlight_text("grey", "  "), highlight_text(guess[0][0], guess[0][0] + " "), highlight_text(guess[0][1], guess[0][1] + " "), highlight_text(guess[0][2], guess[0][2] + " "), highlight_text(guess[0][3], guess[0][3] + " "), highlight_text("grey", "  ")]

    else:
        printed_list[1] = [highlight_text("grey", "  "), highlight_text(guess[0][0], "  "), highlight_text(guess[0][1], "  "), highlight_text(guess[0][2], "  "), highlight_text(guess[0][3], "  "), highlight_text("grey", "  ")]

    for _ in range(6):
        printed_list[2].append(highlight_text("grey", "  "))

    for row in range(len(printed_list)):

        if row in [0, 2]:
            print("               ", end="")
        else:
            print("The answer is: ", end="")

        print("".join(printed_list[row]))

    print(end=f"\n")

def print_board(guesses, feed_back):
    board = []

    for guess in guesses:
        color_list = [color for color in guess]
        board.append(color_list)

    for _ in range(10-(len(guesses))):
        buffer_list = ["  " for _ in range(4)]
        board.append(buffer_list)

    if letters_on_or_off:
        for lines in range(len(board)):
            for color in range(4):
                if board[lines][color] != "  ":
                    board[lines][color] = highlight_text(board[lines][color], board[lines][color].upper() + " ")
    
    else:
        for lines in range(len(board)):
            for color in range(4):
                if board[lines][color] != "  ":
                    board[lines][color] = highlight_text(board[lines][color], "  ")

    for lines in board:
        for ws in range(0, (len(lines) * 2) + 1, 2):
            lines.insert(ws, highlight_text("grey", "  "))
        lines.append(highlight_text("grey", "  "))  

    for ws in range(0, (len(board) * 2) + 1, 2):
        board.insert(ws, [highlight_text("grey", "  ") for _ in range(14)])

    line = 1
    for result in feed_back:
        board[line].append((": " * result[0]) + (". " * result[1]) + ("  " * (4 - (result[0] + result[1]))))
        line += 2

    for _ in range(len(guesses), 10):
        board[line].append("  " * 4)
        line += 2

    for lines in board:
        lines.append(highlight_text("grey", "  "))
        lines.append(highlight_text("grey", "  "))

    row = []

    if letters_on_or_off:
        for abbr in color_abbrs:
            row.append(highlight_text("grey", "  "))
            row.append(highlight_text(abbr, (abbr.upper()) + " "))

    else:
        for abbr in color_abbrs:
            row.append(highlight_text("grey", "  "))
            row.append(highlight_text(abbr, "  "))

    row.append(highlight_text("grey", "  "))

    for lines in board:
        lines.insert(0, (highlight_text("grey", "  ")))
        
    board.append(row)
    board.append(highlight_text("grey", "  ") * 17)

    print("\033c", end="")
    for line in board:
        print("".join(line))
    
    print(end=f"\n")

def menu_choices():
    print("Menu options:")
    print(f"\n  see board: B")
    print("  see remaining solutions: R")
    print("  see suggested guess: S")
    print("  enter guess: G")
    print("  toggle letters on/off: T")
    print("  reset the program: RE")
    print("  end program: CTRL + C", end=f"\n\n")

    print(f"Remaining guesses: {len(list_of_possible_solutions_1)}/{len(color_abbrs)**4}")

    choice = input("Enter choice: ").strip().lower()
    while choice not in ["b", "r", "s", "t", "re", "g"]:

        print("\033c", end="")
        print("Invalid response", end=f"\n")
        print("Menu options:")
        print(f"\n  see board: B")
        print("  see remaining solutions: R")
        print("  see suggested guess: S")
        print("  enter guess: G")
        print("  toggle letters on/off: T")
        print("  reset the program: RE")
        print("  end program: CTRL + C", end=f"\n\n")

        print(f"Remaining guesses: {len(list_of_possible_solutions_1)}/{len(color_abbrs)**4}")

        choice = input("Enter choice: ").strip().lower()

    return choice

def welcome():
    print("\033c", end="")
    print(
        f"""Welcome to Mastermind Solver!

This program helps you solve a Mastermind game (4 pegs, colors can repeat).

How to enter guesses:
Type 4 color letters with NO spaces. Example: rpgy)
Valid letters: R P G Y W B K C

Then enter the feed back:
: = black peg (right color, right spot)
. = white peg (right color, wrong spot)
Examples: ::. :..  it may return no pegs ""

"""
    )
    
    return get_if_letters_on_or_off()

try:
    letters_on_or_off = welcome()

    while True:
        print("\033c", end="")

        join_space = highlight_text("grey", "  ")

        guesses = []
        feed_back_list = []

        list_of_possible_solutions_1 = make_all_possible_guesses()

        while len(list_of_possible_solutions_1) > 1:
            choice = menu_choices()

            if choice != "g":
                print("\033c", end="")

            if choice == "b":
                print_board(guesses, feed_back_list)
            
            elif choice == "r":
                print_remaining_guess(list_of_possible_solutions_1)

            elif choice == "s":
                best_list, best_score = scorer(list_of_possible_solutions_1)
                print_sugggested_quess(best_list, best_score)

            elif choice == "g":
                guess, blacks, whites = get_guess_and_feed_back()
                print("\033c", end="")

                guesses.append(guess)
                feed_back_list.append([blacks, whites])

                list_of_possible_solutions_1 = get_rid_of_impossible_answers(guess, blacks, whites, list_of_possible_solutions_1)

            elif choice == "t":
                letters_on_or_off = not letters_on_or_off

            else:
                break
                   
        if len(list_of_possible_solutions_1) == 1:
            print("\033c", end="")

            if list_of_possible_solutions_1[0] not in guesses:
                guesses.append(list_of_possible_solutions_1[0])
                feed_back_list.append([4, 0])

            print_board(guesses, feed_back_list)
            print_answer(list_of_possible_solutions_1)
            input(f"Press enter to run the program again or Ctrl + C to end the program: ")

except KeyboardInterrupt:
    print("\033c")