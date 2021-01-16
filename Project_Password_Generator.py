    # Password Generator Project
import random
import os
var_loop =  True

def main():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    User_var_random = input("Do you want your password randomised y/N:\n").lower()
    User_var_duplicate = input("Do you want your password to contain duplicates: Y = Duplicates N = No Duplicates:\n").lower()
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    Generated_Password = []
    Generated_Password_letters = []
    Generated_Password_symbols = []
    Generated_Password_numbers = []
    result = " "
    random_list = []

    if User_var_duplicate == "y":
        for letter in range(0, nr_letters):
            x = random.randint(0, len(letters) - 1)
            Generated_Password.append(letters[x])

        for symbol in range(0, nr_symbols):
            x = random.randint(0, len(symbols) - 1)
            Generated_Password.append(symbols[x])

        for number in range(0, nr_numbers):
            x = random.randint(0, len(numbers) - 1)
            Generated_Password.append(numbers[x])
        while len(random_list) < len(Generated_Password):
            x = random.randint(0, len(Generated_Password) - 1)
            random_list.append(Generated_Password[x])

    elif User_var_duplicate == "n":
        while len(Generated_Password_letters) < nr_letters:
            x = random.randint(0, len(letters) - 1)
            if letters[x] not in Generated_Password_letters:
                Generated_Password_letters.append(letters[x])
        while len(Generated_Password_symbols) < nr_symbols:
            x = random.randint(0, len(symbols) - 1)
            if symbols[x] not in Generated_Password_symbols:
                Generated_Password_symbols.append(symbols[x])
        while len(Generated_Password_numbers) < nr_numbers:
            x = random.randint(0, len(numbers) - 1)
            if numbers[x] not in Generated_Password_numbers:
                Generated_Password_numbers.append(numbers[x])
        Generated_Password = Generated_Password_letters + Generated_Password_numbers + Generated_Password_symbols
        random_list = Generated_Password_letters + Generated_Password_numbers + Generated_Password_symbols

    if User_var_random == "y":
        for items in random_list:  #randomisedy
            result += str(items)

    elif User_var_random == "n":
        for items in Generated_Password:  #Not randomised
            result += str(items)
    else:
        print("Unknown Input, please run script again")

    print(f"your password is\n{result}\n")

while var_loop is not False:
    main()
    User_var = input("Do you want to try again y/N: ").lower()

    if User_var == "n":
        var_loop = False
        if os.name == 'nt':
          os.system('cls')
        else:
          os.system('clear')
