import random 
'''

class CoinToss:
    def __init__(self):
        pass
    def main(self):
        try:
            while True:
                self.guess_a_coin()
                self.check_guess()
        except KeyboardInterrupt: print('Closing Coin Toss Game')
    def guess_a_coin(self):
        self.guess = ''
        self.toss = self.toss_a_coin()
        while True:
            self.get_guess()
            if self.guess in ('heads','tails'):
                break
            print('Wrong entry: pick tails or heads')
    def get_guess(self):
        print('Guess the coin toss! Enter heads or tails:')
        self.guess = input()
    def toss_a_coin(self):
        return random.choice(['heads','tails'])
    def check_guess(self):
        if self.guess == self.toss: print('You got it!')
        else:
            print('Nope! Guess again!')



if __name__ == '__main__':
    game = CoinToss()
    game.main()
'''
import random

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

