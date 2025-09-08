#.\python-exercises\practice-programs.py
import time 
def collatz(number):
    if number % 2 == 0:
        return number//2
    else:
        return 3 * number+1
for number in range(1,100):
    time.sleep(0.3)
    print('\n','number:',number,'[',end='')
    while True:
        number = collatz(number)
        if number == 1:
            print(number,end='')
            break
        print(number,', ',end='')
    print(']')

    



