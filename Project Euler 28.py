#def things
def diangle_numbers(side_length):
    sum_of_diangle = 0
    changeing_side = side_length
    for _ in range((side_length // 2) + 1):
        for i in range(4):
            if changeing_side == 1:
                sum_of_diangle += 1
                break
            sum_of_diangle += (changeing_side ** 2) - ((changeing_side - 1) * i)
        changeing_side -= 2
    return sum_of_diangle

print("\033c", end="")
side_len = 2
while side_len % 2 == 0: 
        side_len = int(input("How big do you want the grid to be? Please enter an odd number: "))
print("\033c", end="")
print(f"The diagonals on a spiral with side length {side_len} is {diangle_numbers(side_len)}")