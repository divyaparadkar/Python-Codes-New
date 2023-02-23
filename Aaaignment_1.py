#Q1. 
#*******
#you are in normal function
#********

def dec_star(func):
    def inner():
        print("*"*6)
        func()
        print("*"*6)
    return inner


@dec_star
def normal():
    print("you are in normal function")
normal()