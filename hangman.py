import os, random, image, words

word = 'BLANK'
show = list(len(word)*'_')
lives_remaining = 8
gameWon = False

while gameWon == False and lives_remaining > 0:
    print(show)
    guess = input('Type your guess using a letter or a word:')
    guess = guess.upper()

    if guess == word:
        gameWon = True
    if len(guess) == 1 and guess in word:
        for letter in range(0,len(word)):
            reveal = word[letter] 
            if guess == reveal:
                show[letter] = guess

        if '_' not in show:
            gameWon = True

    else:
        lives_remaining -= 1

if gameWon:
    print('Congratulations! You guessed the correct word. \n')
else:
    print(f'Unlucky you guessed incorrectly! The word was: {word}, try again')

