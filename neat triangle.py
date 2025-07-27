#housekeeping
bomb_list = []
elment = "#"

#def things
def bomb(n, best_n):
    if n >= 1:
        new_list = (" " + elment) * n
        bomb_list.append(str(new_list).center((best_n * 2) - 1))
        bomb(n-1, best_n)
    else:
        return None

#make it loop
try:
    while True:
        
        #clear the list
        bomb_list = []

        #get input
        lenth = int(input(f"Give the number of lines you want the triangle to have: "))

        #clear the screen
        print("\033c", end="")

        #run the program
        bomb(lenth, lenth)

        #print the result
        for bombs in range(len(bomb_list) - 1, -1, -1):
            print("".join(bomb_list[bombs]))

#make it so the program can stop
except KeyboardInterrupt:
    print("\033c", end="")