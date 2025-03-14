import math


user_input = input("Please enter a number: ")


try:
    number = float(user_input)
    rounded_number = math.ceil(number)  
    print(f"The number {user_input} rounded up is: {rounded_number}")
except ValueError:
    print("That's not a valid number.")