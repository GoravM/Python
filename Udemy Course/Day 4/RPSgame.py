import random

RPS = ["Rock","Paper","Scissor"]

uinput = int(input("Type 0 for rock, 1 for paper or 2 for scissors.\n"))
cinput = random.randint(0,2)

if uinput >= 3 or uinput < 0:
    print("Invalid input, you lose")
else:
    mine = RPS[uinput]
    print(mine)

    comp = RPS[cinput]
    print(f"The Computer choose:\n{comp}")

    if cinput == 2 and uinput == 0:
        print("you win")
    elif uinput == 2 and cinput == 0:
        print("you lose")
    elif uinput < cinput:
        print("You lose")
    elif uinput == cinput:
        print("its a draw")
    else:
        print("you win!")
