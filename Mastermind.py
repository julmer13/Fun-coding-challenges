#import things
import random
from colorama import Fore, Style, Back, init

#housekeeping
empty_space = "  "
color_space = "  "
white_space = "  "
black_pegs = ": "
white_pegs = ". "
game_state = False
is_valid = False
guesses = 0
guess_list = []
color_abbrs = ["r", "p", "g", "y", "w", "b"]

#def things
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

def make_board(guesses, answer):
    board = []
    won = False
    for guess in guesses:
        color_list = [color for color in guess]
        board.append(color_list)
    for _ in range(10-(len(guesses))):
        buffer_list = [empty_space for _ in range(4)]
        board.append(buffer_list)
    for lines in range(len(board)):
        for color in range(4):
            if board[lines][color] != empty_space:
                board[lines][color] = highlight_text(board[lines][color], color_space)
    for lines in board:
        for ws in range(0, (len(lines) * 2) + 1, 2):
            lines.insert(ws, highlight_text("grey", white_space))
        lines.append(highlight_text("grey", white_space))  
    for ws in range(0, (len(board) * 2) + 1, 2):
        board.insert(ws, [highlight_text("grey", white_space) for _ in range(14)])
    line = 1
    for guess in guesses:
        blacks = 0
        whites = 0
        test_guesse = guess[:]
        test_answer = answer[:]
        for color in range(4):
            if test_guesse[color] == test_answer[color]:
                blacks += 1
                test_answer[color] = None
                test_guesse[color] = None
        if blacks == 4:
            won = True
        for color in range(4):
            if test_guesse[color] is not None and test_guesse[color] in test_answer:
                whites += 1
                test_answer[test_answer.index(test_guesse[color])] = None
        board[line].append((black_pegs * blacks) + (white_pegs * whites) + ("  " * (4 - (blacks + whites))))
        line += 2
    for _ in range(len(guesses), 10):
        board[line].append("  " * 4)
        line += 2
    for lines in board:
        lines.append(highlight_text("grey", white_space))
    row = []
    row.append(highlight_text("grey", empty_space))
    for abbr in color_abbrs:
        row.append(highlight_text("grey", empty_space))
        row.append(highlight_text(abbr, (abbr.upper()) + " "))
    row.append(highlight_text("grey", empty_space * 2))
    board.append(row)
    board.append(highlight_text("grey", white_space) * 15)
    print("\033c", end="")
    for line in board:
        print("".join(line))
    return won

def make_answer():
    return [random.choice(color_abbrs) for _ in range(4)]

def welcome():
    print("\033c", end="")
    input(f"""Welcome to Mastermind!
To play put in four of the abbreviations for the colors split by spaces.
If you don't know a abbreviation for a color it is at the bottom of the board.
After each guess {black_pegs}and {white_pegs}symbols will show up.
{black_pegs}means that one color is in the right spot.
{white_pegs}means that one color is in the answer but in the wrong spot.
The answer may contain two of one color.
Press enter to contiune: """)

welcome()
answer = make_answer()
while not game_state and guesses < 10:
    game_state = make_board(guess_list, answer)
    if is_valid:
        print("Last guess was invalid please try again:")
        is_valid = False
    if game_state == False:
        guess = (input(f"give me the four abbreviation of colors for your guess split by spaces: ")).split(" ")
        if len(guess) != 4:
            is_valid = True
        for color in guess:
            if color.lower() not in color_abbrs:
                is_valid = True
            color = color.lower()
        if is_valid:
            continue
        guesses += 1
        guess_list.append(guess)

game_state = make_board(guess_list, answer)
row = []
for abbr in answer:
    row.append(highlight_text(abbr, abbr.upper()))
if guesses < 10:
    print(f"You won! You guessed the answer of {' '.join(row)} in {guesses} guesses.")
else:
    print(f"Sorry, you could not guess the answer of {' '.join(row)} in 10 guesses.")
print(f"Thanks for playing!")