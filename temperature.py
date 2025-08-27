#def things
#for celis to farenhight 
def c_to_f(c):
    return (c * 9/5) + 32

#for farenhight
def f_to_c(f):
    return (f - 32) * 5/9

#main program
#get user input
temperature = input(f"Put a number in, with the a c for celis and f for fahrenheit: ")

#detect c or f
if "c" in temperature:
    temperature = float(temperature.replace("c", ""))
    print(f"{temperature} degrees celis in fahrenheit is: {c_to_f(temperature)}")
elif "f" in temperature:
    temperature = float(temperature.replace("f", ""))
    print(f"{temperature} degrees fahrenheit in celis is: {f_to_c(temperature)}")
else:
    print("Invalid input. Please include 'c' for Celsius or 'f' for Fahrenheit.")