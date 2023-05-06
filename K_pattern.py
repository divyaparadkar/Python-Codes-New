e=0
k=4
for i in range(7):
    for j in range(5):
        if j==0 or(i==j+2 and j>1):
            print("*",end="")
        elif((i==e and j==k)and j>0):
            print("*",end="")
            e=e+1
            k=k-1
        else:
            print(end=" ")
    print()