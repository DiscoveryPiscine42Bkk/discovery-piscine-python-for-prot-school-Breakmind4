number = int(input("Please put your number less than 25/n"))

if number >=25 :
    print("This number more than 25")

else:
    while number <=25:
        print(f"Inside the loop, my varible is {number}")
        number += 1