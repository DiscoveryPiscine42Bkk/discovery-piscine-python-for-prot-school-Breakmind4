number1 = int(input("Please enter your first number"))
number2 = int(input("Please enter your second number" ))

result = number1 * number2
print(f"{number1} * {number2} ={result}")

if result > 0:
    print("The result is Positive")
elif result < 0:
    print("The result is Negative")
else:
    print("The result is Negative and Positive")