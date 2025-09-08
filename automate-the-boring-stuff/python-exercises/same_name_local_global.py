def spam():
    global eggs
    eggs = 'spam'   # this is the global variable 

def bacon():
    eggs = 'bacon'  # this is a local variable 

def ham():
    print(eggs)     # this is the global variable 

eggs = 'global'     # this is the global variable 
print(eggs)
spam()
print(eggs)