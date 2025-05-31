#import things
from random import randint
from colorama import Fore, Style, Back, init

#def things
def highlight_text(text):
    highlight_map = {
    "gray": Back.LIGHTBLACK_EX
}
    color_code = highlight_map.get("gray", Fore.RESET)
    return(f"{color_code}{text}{Style.RESET_ALL}")

def make_board(challenge, point_x, point_y):
    bomb_shape = "•"
    if challenge.lower() == "easy":
        board_side = 8
        bombs = 10
    elif challenge.lower() == "medium":
        board_side = 14
        bombs = 40
    else:
        board_side = 20
        bombs = 99
    
    board = [[0 for _ in range(board_side)] for _ in range(board_side)]

    bomb_list = []

    for _ in range(bombs):
        rand_x = randint(0, board_side - 1)
        rand_y = randint(0, board_side - 1)
        board[rand_y][rand_x] = bomb_shape
        bomb_list.append((rand_y, rand_x))
    
    while (point_y, point_x) in bomb_list:
        bomb_list = []

        for _ in range(bombs):
            rand_x = randint(0, board_side - 1)
            rand_y = randint(0, board_side - 1)
            board[rand_y][rand_x] = bomb_shape
            bomb_list.append((rand_y, rand_x))

    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == bomb_shape:
                for square_y in range(y - 1, y + 2):
                    for square_x in range(x - 1, x + 2):
                        if 0 <= square_y < len(board) and 0 <= square_x < len(board[0]):
                            if board[square_y][square_x] != bomb_shape:
                                board[square_y][square_x] += 1

    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 0:
                board[y][x] = " "
            if (x + y) % 2 == 1:
                board[y][x] = highlight_text((" " + str(board[y][x]) + " "))
            else:
                board[y][x] = " " + str(board[y][x]) + " "
            
    return board

make_board("medium", 0, 0)