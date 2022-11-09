def HCF(a, b):
    if (b == 0):
        return abs(a)
    else:
        return  HCF(b, a % b)


a = 60
b = 48

# prints 12
print(" 60 and 48 is : ", end="")
print(HCF(60, 48))