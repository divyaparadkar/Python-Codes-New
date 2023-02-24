x=int(input("Enter first value"))
y=str(input("Enter second value"))
try:
    x += y
    print("hey what is this :) ")
except TypeError:
    print("Hello this is my last line")