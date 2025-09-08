def spam(divide_by):
    try:
        return 42/divide_by
    except ZeroDivisionError:
        return 'Error: invalid argument'

a = 2,12,0,1

for i in a:
    print(spam(i))