import random
from hangman_art import stages, logo
from word_list import word_list

print(logo)
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = raw_input("Guess a letter: ").lower()



    if guess in display:
        print("You've already guessed " + str(guess) + ".")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(' '.join(display))

    if guess not in chosen_word:
        print("You guessed " + str(guess) + ", that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")

    if not "_" in display:
        game_is_finished = True
        print("You win.")

    print(stages[lives])