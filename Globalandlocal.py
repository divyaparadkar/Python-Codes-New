# Global and local variables
a=10
def f1():
    a=777
    print(a)
    print(globals()['a'])
f1()


a=30
def f1():
    a=47
    print(a)
    print(globals()['a'])
f1()