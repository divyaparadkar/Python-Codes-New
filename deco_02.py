def decor1(func1):
    def inner():
        x=func1()
        return(x*x)
    return inner
def decor2(func2):
    def inner():
        x=func2()
        return(2*x)
    return inner
@decor1
@decor2
def fun():
    return(10)
print(fun())
