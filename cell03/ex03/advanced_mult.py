number1 = int(input("First_number"))
number2 = int(input("Second number"))
result = number1 * number2
if result > 0:
    print(f"{number1} x {number2} = {result}")
    print("The result is positive")
if result < 0:
    print(f"{number1} x {number2} = {result}")
    print("The result is negative")
else:
    print(f"{number1} x {number2} = {result}")
    print("The result is positive and negative")