def spam():
    global eggs
    eggs = 'spam' # This is the global

def bacon():
    eggs = 'bacon' # this a local
def ham():
    print(eggs) # This is a global

eggs = 42 # This is a gobal
spam()
print(eggs)
