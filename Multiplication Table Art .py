#housekeeping
symbol_list = ["&", "#", "@", "%", "+"]

#def things
def make_grid(size):
    for y in range(size):
        for x in range(size):
            index = (((y + 1) * (x + 1)) % len(symbol_list))
            grid[y][x] = symbol_list[index]
size_side = int(input(f"Give me the length of the side: "))
grid = [[" " for _ in range(size_side)] for _ in range(size_side)]
make_grid(size_side)
for line in grid:
    print(" ".join(line))