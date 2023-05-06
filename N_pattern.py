for i in range(7):
    for j in range(7):
        if j==0 or j==5 or(i==j and (j>0 and j<5)):
          print("*",end="")
        else:
           print(end=" ")
    print()