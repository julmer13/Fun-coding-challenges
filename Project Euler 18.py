#import things
import os

#def things
def Best_path_through_triangle(triangle):
    for y in range(len(triangle) - 2, -1, -1):
        for x in range(len(triangle[y])):
            triangle[y][x] += max(triangle[y + 1][x], triangle[y + 1][x + 1])
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"The best way down gives a sum of {triangle[0][0]}")

os.system('cls' if os.name == 'nt' else 'clear')
print('Give me the triangle line by line then type done after: ' )
lines = []
while True:
    line = input()
    if line.upper() == "DONE":
        break
    lines.append(line)
Best_path_through_triangle([list(map(int, row.split())) for row in lines])