# Update/ Insert - List

mylist =[1,2,3,4,5,6]
print(mylist)
mylist[3]=34 
mylist[0]=56
print(mylist)


mylist =[1,2,3,4,5,6]
print(mylist)
mylist.insert(4,24) #insert method ------------> O(n)
print(mylist)

mylist.append(55)# append method------------>O(1)

newlist=[12,23,34,67,78]
mylist.extend(newlist)#extend method ----------->O(n)
print(mylist)
