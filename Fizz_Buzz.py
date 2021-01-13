User_var = int(input("Please enter a number: Fizz Buzz!!: "))

for var in range(0, User_var + 1):
    if var % 3 == 0 and var % 5 == 0:
        print("FizzBuzz")
    elif var % 3 == 0:
        print("Fizz")
    elif var % 5 == 0:
        print("Buzz")
    else:
        print(var)