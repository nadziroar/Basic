import random
secretNum = random.randint(1, 100)
print('I am thinking number from 1 - 100')


#Ask the player to guess 6 times
for guessno in range(1, 7):
    print('Guess the no : ')
    guess = int(input())

    if guess < secretNum:
        print('Too low babe')
    elif guess > secretNum:
        print('Too high babe')
    else:
        break

if guess == secretNum :
    print('Good job! You guessed the right no: ' + str(guessno) + ' guesses!')
else:
    print('Nope. The number i was thinking of was :  ' + str(secretNum))
