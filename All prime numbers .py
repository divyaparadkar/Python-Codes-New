#print all prime numbers in an interval
#{2,3,5,7,11,.......}.
num=int(input())
for i in range(2,num):
    if num %i==0:
        print("Not prime")
        break
else:
    print("prime")