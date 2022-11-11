#A FORMULA.A=P(1+R/100)
#CI FORMULA A-P
print("principle is :")
P=int(input())
print("rate is :")
R=int(input())
print("time is :")
T=int(input())
A=P*(1+(R/100))**T
CI= A-P
print("Compound intrest is :",CI)