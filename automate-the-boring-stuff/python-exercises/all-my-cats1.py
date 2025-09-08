cats = [] 
count = 1
for i in range(4):
    cats.append(input(f'Enter the name of cat {count}: '))
    count += 1
print('here are the names of your cats')
for i in cats: print(i,' ',end='')

