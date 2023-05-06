for i in range(7):
    for j in range(5):
        if j==0 or (i==6 and j>0):
            print("*",end="")
        else:
            print(end=" ")
    print()
        