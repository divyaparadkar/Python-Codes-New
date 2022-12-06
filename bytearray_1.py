elements = [12, 34, 67, 91, 12, 89, 3]
x=bytearray(elements)
x[3]=45
x[0]=43
x[1]=44
x[4]=46
for i in x:
    print(i)
