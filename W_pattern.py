e=0
f=3
for i in range(4):
    for j in range(7):
        if j==0 or j==6 or(j==5 and i==2) or (j==4 and i==1):
            print("*",end="")
        elif i==e and j==f:
            print("*",end="")
            e=e+1
            f=f-1
        else:
            print(end=" ")
    print()