#program to make a simple calculator
#take input
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
#choise operation
print("Operation:+,-,*,/")
select =input("Select operations:")
#add
if select =="+":
    print(num1,"+",num2,"=",num1+num2)
#sub
elif select =="-":
    print(num1,"-",num2,"=",num1-num2)
#mul
elif select =="*":
    print(num1,"*",num2,"=",num1*num2)
#div
elif select =="/":
    print(num1,"/",num2,"=",num1/num2)
else:
    print("Invalid input")
