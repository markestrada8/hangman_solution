from data import words
import random

words_list = [word for word in words.split('\n')[:-1]]
word = random.choice(words_list)

game_on = True

print('Welcome to Hangman!')
guesses = 8
blanks = []
for letter in word:
    blanks.append('_')


while game_on:
    print(f'Your word is: {"".join(blanks)}')
    print(f'You have {guesses} guesses')
    choice = input("Enter your guess: \n")

    if choice in word:
        for i in range(len(word)):
            if word[i] == choice:
                blanks[i] = choice
        print("That's right!\n")
    else:
        guesses -= 1
        print('\nSorry, lost a guess\n')
    if guesses == 0:
        print('Game over')
        game_on = False
    if '_' not in blanks:
        print(f'Your word was: {word}!')
        print('You Win!!!!')
        game_on = False
    print('\n' * 2)
print('Thanks for playing!')
