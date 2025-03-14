num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))

#Perform the calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
#Check if the second number is not zero to avoid division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "undefined (cannot divide by zero)"

#Display the results
print(f"The result of {num1} + {num2} is: {addition}")
print(f"The result of {num1} - {num2} is: {subtraction}")
print(f"The result of {num1} * {num2} is: {multiplication}")
print(f"The result of {num1} / {num2} is: {division}")