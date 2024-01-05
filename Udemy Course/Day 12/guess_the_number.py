import random

def guessing_game(attempts):
    game_end = False
    number = random.randrange(0,100)
    # print(number)
    while not game_end:
        
        if (attempts > 0):

            guess = int(input(f"You have {attempts} attempts remaining to guess the number. \nMake a Guess: "))

            if guess > number:
                print("Too High.")
                attempts -= 1
                if attempts >= 1:
                    print("Guess again")
            elif guess < number:
                print("Too Low.")
                attempts -= 1
                if attempts >= 1:
                    print("Guess again")
            elif guess == number:
                print(f"You got it! The answer was {number}")
                game_end = True

        if attempts == 0:
            print("You've run out of guessses, you lose.")
            game_end = True
            
print("Welcome to the Number Guessing Game! \nI'm Thinking of a number between 1 and 100." )

difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard': "))

if difficulty == "easy":
    guessing_game(attempts= 10)

elif difficulty == "hard":
    guessing_game(attempts= 5)

