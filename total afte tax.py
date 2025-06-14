print("\033c", end="")
inputs = (input(f"Give me the after tax number and the tax split by a space: ")).split(" ")
print("\033c", end="")
print(f"To get {inputs[0]} after a {inputs[1]}% tax you need to get: {int(inputs[0]) / (1 - (int(inputs[1]) / 100))}")