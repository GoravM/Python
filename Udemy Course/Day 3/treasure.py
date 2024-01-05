print("Welcome to Treasure Island. Your mision is to find the treasure.")
choice1 = input("Left or right? ").lower()

if choice1 == "left":
    choice2 = input("Swim or Wait? ").lower()

    if choice2 == "wait":
        choice3 = input("Which door? Red, Yellow, or Blue? ").lower()

        if choice3 == "red":
            print("You got lit on fire")

        elif choice3 == "yellow":
            print("You Win!")

        elif choice3 == "blue":
            print("You got molested")
            
        else:
            print("You got molested")
    else:
        print("You Drowned")
else:
    print("You got ran over by a car")