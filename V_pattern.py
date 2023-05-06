e=0
f=6
for i in range(4):
    for j in range(7):
        if i==j:
           print("*",end="")
        elif i==e and j==f:
            print("*", end=" ")
            e=e+1
            f=f-1
        else:
            print(end=" ")

    print()