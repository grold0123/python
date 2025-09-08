#.\python-exercises\guess-the-number.py
 
'''
output 
I am thinking of a number between 1 and 20.
Take a guess.
>10
Your guess is too low.
Take a guess.
>15
Your guess is too low.
Take a guess.
>17
Your guess is too high.
Take a guess.
>16
Good job! You got it in 4 guesses!
'''
import random
the_number = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')
print('Take a guess.')
guess = 0
while True:
    guess = input('>')
    guess_count += 1
    if guess == the_number: break
    elif guess < the_number: print('Your guess is too low.')
    elif guess > the_number: print('Your guess is too high.')
print(f'Good job! You got it in {guess_count} guesses!')