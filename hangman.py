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

    # While loop begins
    while not gameWon and lives_remaining > 0:
        guess = input("Type your guess using a letter or a word:").upper()
        # Clear the game board so that out command window is cleaner.
        clear_screen()
        # Check if the length of the guess is just 1 letter,
        # Also if the guess is in the alphabet.
        if len(guess) == 1 and guess.isalpha():
            if guess in used_letters:
                print(f"This letter {guess} has already been guessed.")               
            elif guess not in word:
                print(f"This letter {guess} is not in the chosen word.")
                # Remove a life if the guess is incorrect
                lives_remaining -= 1
                used_letters.append(guess)
            else:
                print(f"Fantastic, {guess} is in the chosen word!")
                used_letters.append(guess)
                listed_words = list(show)
                # Reveal the guessed letter from the word
                # in the correct location.
                reveal = [i for i, letter in enumerate(word) if letter == guess]
                # show every guess occurence.
                for index in reveal:
                    listed_words[index] = guess
                show = "".join(listed_words)
                if "_" not in show:
                    gameWon = True
        

