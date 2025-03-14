user_input = input("Please enter your number: ")


try:
    number = float(user_input)

    if number.is_integer():
        print(f"The number {user_input} is not a decimal.")
    else:
        print(f"The number {user_input} is a decimal.")
except ValueError:
    print("That's not a valid number.")