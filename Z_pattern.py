e=1
f=4
for i in range(0,6):
    for j in range(0,6):
        if i==0 or i==5:
            print("*",end="")
        elif i==e and j==f:
            print("*",end="")
            e=e+1
            f=f-1
        else:
            print(end=" ")
    print()

