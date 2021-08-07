# Import files that will be used in my program
import random
from image import hanging_man, welcome
from words import random_words

# Variables used throught hangman.
word = random.choice(random_words)
word = word.upper()
show = list(len(word)*'_')
lives_remaining = 8
gameWon = False


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


# Create the playing board this is what users can see.
def hangman_board():
    """
    Printing the users game board to the screen
    this will include the hangman image, unrevealed word
    and lives remaining.
    """
    clear_screen()
    print("WELCOME TO HANGMAN!")
    print(hanging_man[8-lives_remaining])
    print(" ".join([str(i) for i in show]))
    print(f'You have {lives_remaining} lives remaining!')


# checking if a letter or word we guessed is correct or incorrect.
while gameWon is False and lives_remaining > 0:
    hangman_board()
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
    hangman_board()

# win or lose statment
if gameWon:
    print('Congratulations! You guessed the correct word. \n')
else:
    print(f'Unlucky you guessed incorrectly! The word was: {word}, try again')
