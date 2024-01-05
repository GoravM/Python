from game_data import data
import random

def format_data(account):
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return (f"{account_name}, a {account_desc}, from {account_country} ")

def get_followers(account):
    account_fol = account['follower_count']
    return account_fol

def play_game():
    score = 0
    game_end = False

    account_a = random.choice(data)
    account_b = random.choice(data)

    while not game_end:

        print()
        print(f"{format_data(account_a)}")
        print("VS")
        print(f"{format_data(account_b)}")
        guess = input("Who has more followers? Type 'A' or 'B': ")

        if guess == "A":
            if get_followers(account_a) > get_followers(account_b):
                score += 1
                print(f"Correct!, your score is {score}")
                account_b = random.choice(data)

            elif get_followers(account_a) == get_followers(account_b):
                score += 1
                print(f"Correct!, your score is {score}")
                account_b = random.choice(data)

            else:
                game_end = True
                print(f"You ended with a score of {score}")

        elif guess == "B":
            if get_followers(account_a) < get_followers(account_b):
                score += 1
                print(f"Correct!, your score is {score}")
                account_a = account_b
                account_b = random.choice(data)

            elif get_followers(account_a) == get_followers(account_b):
                score += 1
                print(f"Correct!, your score is {score}")
                account_b = random.choice(data)

            else:
                game_end = True
                print(f"You ended with a score of {score}")

        else:
            game_end = True

play_game()
