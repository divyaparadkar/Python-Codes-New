def fun():
    yield"a"
    yield"b"
    yield"c"
    yield"d"
f=fun()
print(f)
print(type(f))
print(type(fun))