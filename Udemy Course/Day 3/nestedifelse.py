print("Welcome to the rollercoaster!")
height = int(input("How tall are you? "))

if height > 120:
    print("You can ride the rollercoaster.")
    age = int(input("How old are you? "))

    if age > 18:
        print("Please pay $12.")

    elif 12 <= age <= 18:
        print("Please pay $7.")

    else:
        print("Please pay $5.")
else:
    print("You cannot ride the rollercoaster.")
