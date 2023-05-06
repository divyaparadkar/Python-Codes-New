for i in range(8):
    for j in range(5):
        if ((j==0 or j==4) and (i>0 and i<6))or ((i==0 or i==6) and (j>0 and j<4))or (i==5 and j==1)or (i==7 and j==3):
           print("*",end="")
        else:
            print(end=" ")
    print()