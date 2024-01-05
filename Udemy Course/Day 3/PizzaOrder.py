print("Thank you for choosing Python Pizza Deliveries!")
size = input("What pizza size do you want? (S, M, or L) ")
peperoni = input("Do you want peperonies? (Y or N) ")
exCheese = input("Do you want extra cheese? (Y or N) ")
###############################################################

bill = 0

if size == "S":
    bill += 15

elif size == "M":
    bill += 20

elif size == "L":
    bill += 25

if peperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if exCheese == "Y":
    bill += 1

print(f"{bill}")