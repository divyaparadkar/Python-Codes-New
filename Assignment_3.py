# ***********
# %%%%%%%%%%%
# ###########
# normal function 
# ###########
# %%%%%%%%%%%
# ************

def deco_start(func):
    def inner():
        print("*"*5)
        func()
        print("*"*5)
    return inner



def deco_per(func):
    def inner():
        print("%"*5)
        func()
        print("%"*5)
    return inner



def deco_hash(func):
    def inner():
        print("#"*5)
        func()
        print("#"*5)
    return inner



@deco_start
@deco_per
@deco_hash

def normal():
    print("normal function")
normal()