#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
passwd = ""
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for letter in range(0,nr_letters):
    l = random.randint(0,26)
    passwd += " " + letters[l]
for symbol in range(0,nr_symbols):
    s = random.randint(0,8)
    passwd += " " + symbols[s]
for number in range(0,nr_numbers):
    n = random.randint(0,nr_numbers)
    passwd += " " + numbers[n]
total_char = nr_letters+nr_numbers+nr_symbols
list=passwd.split()
final_pass=""
random.shuffle(list)
for i in range(0,total_char):
    final_pass += list[i]
print(f"Your uncrackable password is: {final_pass}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P