n= int(input("number of elements to taken average of :"))
l=[]
for i in range(1,n+1):
    element = int(input("Enter the element:"))
    l.append(element)
average = sum(l)/n
print("Average of the element in list ",round(average, 2))
