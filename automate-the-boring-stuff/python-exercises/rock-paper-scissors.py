'''
output:
____________________________________________________
ROCK, PAPER, SCISSORS
0 Wins, 0 Losses, 0 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
>p
PAPER versus...
PAPER
It is a tie!
0 Wins, 0 Losses, 1 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
>s
SCISSORS versus...
PAPER
You win!
1 Wins, 0 Losses, 1 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
>q
____________________________________________________
''' 
import random
def display_score(tally):
    wins,losses,ties = tally
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')
def win(tally):tally[0]+=1
def loss(tally):tally[1]+=1
def tie(tally):tally[2]+=1
def equivalent(hand):
    _ = ''
    if hand == 'r': _ = 'ROCK'
    elif hand == 'p': _ = 'PAPER'
    elif hand == 's': _ = 'SCISSORS'
    return _
def display_hands(computer,user):
    user_hand = equivalent(user)
    computer_hand = equivalent(computer)
    print(f'{user_hand} versus...\n{computer_hand}')
def game_start():
    print('ROCK, PAPER, SCISSORS')
    tally = [0,0,0]
    while True:
        computer_move = random.choice(['r','p','s'])
        display_score(tally)
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        user_input = input('>')
        if user_input == 'q': break
        elif user_input == 'r': 
            display_hands(computer_move,user_input)
            if computer_move == 's': win(tally)
            elif computer_move == 'r' : tie(tally)
            elif computer_move == 'p' : loss(tally)
        elif user_input == 'p': 
            display_hands(computer_move,user_input)
            if computer_move == 'r': win(tally)
            elif computer_move == 'p' : tie(tally)
            elif computer_move == 's' : loss(tally)
        elif user_input == 's': 
            display_hands(computer_move,user_input)
            if computer_move == 'p': win(tally)
            elif computer_move == 's' : tie(tally)
            elif computer_move == 'r' : loss(tally)
        print()
    print('Thanks for playing!')

game_start()

