import random 
def get_answer(answer_number):
    #returns a fortune answer based on what int answer_number 
    answers = [
        'It is certain',
        'It is decidedly so',
        'Yes',
        'Reply hazy try again',
        'Ask again later',
        'Concentrate and ask again',
        'My reply is no',
        'Outlook not so good',
        'Very doubtful'
    ]
    if answer_number in range(1,10):
        return answers[answer_number-1]
print('Ask a yes or no question:')
input('>')
r = random.randint(1,9)
fortune = get_answer(r)
print(fortune)

