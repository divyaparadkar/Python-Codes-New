x=int(input("Enter first value"))
y=int(input("Enter second value"))
try:
    z=x/y
    print("division result",z)
except ZeroDivisionError:
    print("invalid attemp of division ")
print("Hello this is my last line")