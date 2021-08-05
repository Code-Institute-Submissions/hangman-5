# Import files that will be used in my program
import random
from os import system, name
from image import hanging_man

#Variables used to crate the program
word = 'BLANK'
show = list(len(word)*'_')
lives_remaining = 8
gameWon = False


def checking_guess(reveal, word):
    """
    When a user inputs a guess of any letter this function will check
    if the letter is part of the word and if so reveal that letter.
    """
    # This is a global variable
    global show

    # This section reveals a correctly guessed letter
    for letter in range(0,len(word)):
        reveal = word[letter] 
        if guess == reveal:
            show[letter] = guess

    if '_' not in show:
        return True
    else:
        return False


def clear_screen():
    print('\033[H\033[J', end='')


def hangman_board():
    clear_screen()
    print(hanging_man[8-lives_remaining])
    print(show)



#def gameWon():


#def validation():



#GameWon will become a function this does all the work 
#checking if a letter or word we guessed is correct or incorrect. 
while gameWon == False and lives_remaining > 0:
    hangman_board()
    guess = input('Type your guess using a letter or a word:')
    guess = guess.upper()

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