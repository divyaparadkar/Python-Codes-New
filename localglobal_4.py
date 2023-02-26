x=int(input("Enter any number here"))
def f1():
    x=8
    print("8 is local variable",x)
def f2(func):
    print(x)
    func()
    print("decorator",x)
@f2
def normal():
    print("normal function")
f1()
normal()


