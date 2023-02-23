# *********
# %%%%%%%%%
# hello
# %%%%%%%%%
# **********
def deco_star(func):
    def inner():
        print("*"*7)
        func()
        print("*"*7)
    return inner


def deco_hash(func):
    def inner():
        print("%"*7)
        func()
        print("%"*7)
    return inner


@deco_star
@deco_hash


def normal():
    print("hello")
normal()