print("Welcome to the rollercoaster!")
height = int(input("How tall are you? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster.")
    age = int(input("How old are you? "))

    if 45 <= age and age <= 55:
        bill = 0
        print("Your ticket is $0.")

    elif age > 18:
        bill = 12
        print("Adult tickets are $12.")

    elif 12 <= age <= 18:
        bill = 7
        print("Youths tickets are $7.")

    else:
        bill = 5
        print("Child tickets are $5.")
    
    wants_photo = input("Do you want a photo taken? Y or N. ")

    if wants_photo == "Y":
        bill += 3

    print(f"Your ticket price is ${bill}")

else:
    print("You cannot ride the rollercoaster.")
