# Import files that will be used in my program
import random
from image import hanging_man, welcome
from words import random_words


def choose_word():
    """
    Pick out a random word from the list of words
    on our words file.
    """
    word = random.choice(random_words)
    # Display the whole word in uppercase.
    return word.upper()


def clear_screen():
    """
    This function clears the console each time a user makes a guess to keep
    the console clean.
    """
    print('\033[H\033[J', end='')


def play(word):
    """
    create while loop to run the game until the secret word is guessed
    or player runs out of lives_remaining.
    Also contains three possible conditions each based on different input.
    Guessing a letter, word or input that is not a letter or word of
    same length as secret word.
    """
    # Variables used through the program.
    show = "_" * len(word)
    gameWon = False
    used_letters = []
    used_words = []
    lives_remaining = 8

    # checking if a letter or word we guessed is correct or incorrect.
    while gameWon is False and lives_remaining > 0:
        guess = input('Type your guess using a letter or a word:').upper()

# This section reveals a correctly guessed letter
        if guess == word:
            gameWon = True
            show = word
        if len(guess) == 1 and guess in word:
            gameWon = checking_guess(guess, word)
# remove a life if a letter or word is guessed incorrectly.
        else:
            lives_remaining -= 1

# win or lose statment
    if gameWon:
        print('Congratulations! You guessed the correct word. \n')
    else:
        print(f'Unlucky you guessed incorrectly! The word was: {word}, try again')




