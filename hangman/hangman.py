from hangman.words import words
import random


def get_valid_word():

    word = random.choice(words)

    while not word.isalpha():
        word = random.choice(words)

    return word


def guess_letter(guess, word_remaining, word):

    new_word_remaining = ""
    lose = False

    for i in range(len(word)):
        if word_remaining[i] != "_":
            new_word_remaining = new_word_remaining + word_remaining[i]

        elif word_remaining[i] == "_" and word[i] == guess:
            new_word_remaining = new_word_remaining + guess

        else:
            new_word_remaining = new_word_remaining + "_"

    if guess not in word:
        lose = True

    return new_word_remaining, lose


def hangman():

    # initialise the game
    word = get_valid_word()
    word_remaining = ""
    for i in range(len(word)):
        word_remaining = word_remaining + "_"

    print(f"The word is: {word_remaining}, you have 3 tries")
    loss_count = 0
    max_losses = 3
    lose = False
    print(word)
    # guess the letters

    while word_remaining != word:
        print(word_remaining)
        guess = input("Guess your letter: ")
        # Check if letter is valid
        while len(guess) > 1 or not guess.isalpha():
            print("You can only guess 1 letter")
            guess = input("Guess your letter: ")
        word_remaining, lose = guess_letter(guess, word_remaining, word)
        if loss_count == 3:
            print(f"You lose, the word was {word}")
            return
        if lose:
            loss_count = loss_count + 1
            print(f"You have {max_losses - loss_count} tries remaining")

    print(f"You win! The word was {word}")


hangman()
