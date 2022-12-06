#program to understand bytearray type array
#creat a list of byte numbers
elements = [10, 20, 30, 0, 40, 50]

#convert the list into bytearray type array
x=bytearray(elements)
x[0] = 89
x[4] = 77
x[3] = 7

for i in x:
    print(i)
