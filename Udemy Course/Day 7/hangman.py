import random
import hangman_words
import hangman_art

chosen_word = str(random.choice(hangman_words.word_list))
word_length = len(chosen_word)

# print(hangman_art.logo)

# print(f"Answer is {chosen_word}")

display = []

for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False

lives = 6

while not end_of_game:

    guess = str(input("Guess a letter ")).lower()

    if (guess in display):
        print(f"You've already guesses {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in word! you have {lives}# of tries left")
        if lives <= 0:
            end_of_game = True
            print("You lose")

    print(f"{' ' .join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win!")
    
    print(hangman_art.stages[lives])