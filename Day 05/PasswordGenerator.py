import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Version: Provide the sequenced password

final_password = ""

for counter in range(nr_letters):
    final_password += random.choice(letters)

for counter in range(nr_symbols):
    final_password+= random.choice(symbols)


for counter in range(nr_numbers):
    final_password+= random.choice(numbers)

#print(f"Your password is: {final_password}")

# Hard Version: shuffle the password
password_list = list(final_password)
print(password_list)

random.shuffle(password_list)
print(password_list)

print(f"Your password is: {"".join(password_list)}")
