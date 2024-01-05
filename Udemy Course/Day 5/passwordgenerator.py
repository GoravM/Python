import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
           'r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H',
           'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','#','$','%','&','(',')','*','+']

############################################################################

print("Welcome to the PyPassword Generator!")
Lnum = int(input("How many letters would you like in your password?\n"))
Nnum = int(input("How many numbers would you like?\n"))
Snum = int(input("How many symbols would you like?\n"))


passwordlist = []

for char in range(1,Lnum + 1):
    passwordlist += str(random.choice(letters))

for char in range(1,Nnum + 1):
    passwordlist += str(random.choice(numbers))

for char in range(1,Snum + 1):
    passwordlist += str(random.choice(symbols))

random.shuffle(passwordlist)

finalpassword = ""

for n in passwordlist:
    finalpassword += n

print(f"your password is {finalpassword}")