#def things
def distinct_powers(top_value_a, top_value_b):
    number_list = []
    for A in range(2, top_value_a + 1, 1):
        for B in range(2, top_value_b + 1, 1):
            if str((A ** B)) not in number_list:
                number_list.append(str(A ** B))
    return len(number_list)

print("\033c", end="")
a = int(input("Give me the top value for A: "))
b = int(input("Give me the top value for B: "))
number_list = distinct_powers(a, b)
print("\033c", end="")
print(f"The total number of distinct powers is: {number_list}")