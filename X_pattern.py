e=0
f=4
for i in range(5):
    for j in range(5):
        if i==e and j==f:
            print("*",end="")
            e=e+1
            f=f-1
        elif i==j:
            print("*",end="")
        else:
            print(end=" ")
    print()