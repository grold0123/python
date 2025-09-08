import random 
count = [0,0]
for i in range(100): # perform 100 coin flips
    if random.randint(0,1) == 0:
        print('H ',end='')
        count[0] +=1
    else:
        print('T ',end='')
        count[1] +=1
print()
print('HEADS:',count[0],'TAILS:',count[1])