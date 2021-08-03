import os, random, image, words

word = 'BLANK'
show = list(len(word)*'_')
print(show)
lives_remaining = 8
gameWon = False

while gameWon == False:
    guess = input('Type your guess using a letter or a word:')
    guess = guess.upper()

    if guess == word:
        gameWon = True

if gameWon:
    print('Congratulations! You guessed the correct word. \n')
else:
    print(f'Unlucky you guessed incorrectly! The word was: {word}, try again')

