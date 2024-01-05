import random

list_string = "Gorav, Ibbi, Edwin, Gurjap"
names = list_string.split(", ")
# pick a random name

num = len(names)

pos = random.randint(0,num -1)

print(f"{names[pos]} is Gay")