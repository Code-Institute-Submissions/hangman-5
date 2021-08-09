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
    create while loop to run the game until the chosen word is guessed
    or player runs out of lives_remaining.
    There are different conditions based on validation.
    Guessing a letter, word or input that is not a letter or word of
    same length as chosen word.
    """
    # Variables used through the program.
    show = "_" + "" * len(word)
    gameWon = False
    used_letters = []
    used_words = []
    lives_remaining = 8

    clear_screen()

    # Short instrctions for how the game is played
    print(welcome)
    print("-------------------------------------------------- ")
    print("Welcome, we hope you enjoy!")
    print("A row of underscores will show how many letter the word has.")
    print("If you guess a letter that is in the hidden word,")
    print("the letter will then be displayed instead of an underscore")
    print("in the correct position.")
    print("You will have 8 lives. Good Luck!")
    print("-------------------------------------------------- ")
    # Create a username before playing hangman.
    username = input("Please Enter A Username: \n")
    print(f"Hello {username}, let's play Hangman. Good Luck!")
    print("--------------------------------------------------- \n")
    # Load up the main game board to begin playing hangman.
    print(hanging_man[8-lives_remaining])
    print(f"YOUR WORD: {show}")
    print("\n")
    print(f"You have {lives_remaining} lives remaining")
    print("\n")

    # While loop begins
    while not gameWon and lives_remaining > 0:
        guess = input("Type your guess using a letter or a word:").upper()
        # Clear the game board so that out command window is cleaner.
        clear_screen()
        # Check if the length of the guess is just 1 letter,
        # Also if the guess is in the alphabet.
        if len(guess) == 1 and guess.isalpha():
            if guess in used_letters:
                print(f"The letter {guess} has already been guessed.")
            elif guess not in word:
                print(f"The letter {guess} is not in the chosen word.")
                # Remove a life if the guess is incorrect
                lives_remaining -= 1
                used_letters.append(guess)
            else:
                print(f"Fantastic, {guess} is in the chosen word!")
                used_letters.append(guess)
                listed_words = list(show)
                # Reveal the guessed letter from the word
                # in the correct location.
                rev = [i for i, letter in enumerate(word) if letter == guess]
                # show every guess occurence.
                for index in rev:
                    listed_words[index] = guess
                show = "".join(listed_words)
                if "_" not in show:
                    gameWon = True
        # Check if the guess is a word and
        # all letters are in the aplhabet.
        elif len(guess) == len(word) and guess.isalpha():
            if guess in used_words:
                print(f"{guess} has already been guessed.")
            elif guess != word:
                print(f"{guess} is not the chosen word.")
                # Remove a life
                lives_remaining -= 1
                used_words.append(guess)
            else:
                gameWon = True
                show = word
        else:
            print("Guess is not valid. Please try again!")

        # Print after all checks.
        print(hanging_man[8-lives_remaining])
        print(f"YOUR WORD: {show}")
        print("\n")
        print(f"You have {lives_remaining}, lives remaining")
        print("\n")

    # Once you have won or lost display a message.
    if gameWon:
        print("Congratulations! You guessed the correct word.\n")
    else:
        print("Unlucky you guessed incorrectly!")
        print(f"The word was: {word}, try again.")
        print("\n")


def main():
    """
    To begin the game for the first time and to see if you would wish
    to continue playing once the first game has ended.
    """
    word = choose_word()
    play(word)
    while input("Would you like to Play Again? (Y/N) \n").upper() == "Y":
        word = choose_word()
        play(word)


# code frame so that program is able
# to run script on command line
if __name__ == "__main__":
    main()
