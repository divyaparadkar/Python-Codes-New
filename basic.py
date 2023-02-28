# Lcm in py

a= int(input("Enter the first value"))
b= int(input("Enter the second value"))

maxNum =max(a,b)
while (True):
    if (maxNum%a == 0)&(maxNum%b ==0):
        break
    maxNum=maxNum+1
print("lcm of{a}and{b} is",maxNum)


#prime or not

a= int(input("Enter the value"))

for i in range(2,a):
    if a %i ==0:
        print("is  not prime")
        break
else:
    print("is prime")