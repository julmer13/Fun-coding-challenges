print("\033c", end="")
grade = int(input(f"What grade are you in: "))
st_age = int(input(f"What age did you start school: "))
did_skip = input(f"Did you skip a grade(s) y/n: ")
if did_skip.lower == "y":
    Diffenece = int(input(f"How many grads did you skip: "))
else:
    Diffenece = 0
print("\033c", end="")
age = (st_age + grade) - Diffenece
print(f"You are either {age} or {age + 1}.")