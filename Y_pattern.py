for i in range(5):
    for j in range(5):
        if (j==2 and i>1) or (i==j and j<2)or (i==0 and j==4) or (i==1 and j==3):
           print("*",end="")
        else:
            print(end=" ")
    print()