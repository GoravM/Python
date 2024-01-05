import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(deck):
    if sum(deck) == 21 and len(deck) == 2:
        return 0
    
    if 11 in deck and sum(deck) > 21:
        deck.remove(11)
        deck.append(1)
    return sum(deck)

def outcome(my_score, dealer_score):
    if my_score > 21 and dealer_score > 21:
        return "You went over, you lose"
    
    if my_score == dealer_score:
        return "Draw"
    elif my_score == 0:
        return "You Win with a BlackJack"
    elif dealer_score == 0:
        return "You Lose, Dealer has a BlackJack"
    elif my_score > 21:
        return "You Lose, You went over 21"
    elif dealer_score > 21:
        return "You Win, Dealer went over 21"
    elif my_score > dealer_score:
        return "You Win"
    else:
        return "You Lose"
    
def play_game():
    my_cards = []
    dealer_cards = []
    game_end = False

    for _ in range(0,2):
        my_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not game_end:
        my_score = calculate_score(my_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f" Your Cards: {my_cards}, Score: {my_score}")
        print(f" Dealer's first Card: {dealer_cards[0]}")

        if my_score == 0 or dealer_cards == 0 or my_score > 21:
            game_end = True
        else:
            user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_choice == "y":
                my_cards.append(deal_card())
            else:
                game_end = True
    
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your final hand: {my_cards}, final score: {my_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(outcome(my_score= my_score, dealer_score= dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":

    play_game()