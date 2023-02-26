# Exception handling in python 

# 1. SyntaxError
# 2. RuntimeError
# 3. try 
# 4. except
# 5.finally
# 6.raise

# default exceptional error.

#using finally

x=int(input("Enter first value "))
y=int(input("Enter second value"))

try:
    z=x/y
    print("result is", z)
except ZeroDivisionError:
    print("::::ZeroDivisionError:::::")
finally:
    print("finally")
print("hello this is my last line")