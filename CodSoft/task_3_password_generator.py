import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("Welcome to password generator!")

no_of_letters = int(input("How many letters would you like to in your password?\n"))
no_of_numbers = int(input("How many numbers would you like to in your password?\n"))
no_of_symbols = int(input("How many symbols would you like to in your password?\n"))

password_list = []
for char in range(1, no_of_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, no_of_numbers + 1):
    password_list.append(random.choice(numbers))
for char in range(1, no_of_symbols + 1):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")
