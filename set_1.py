s ={1, 3, 5, 6, 7, 8, 10,'some','some', 6}
print(s)#set does not store duplicate elements.
s.update([23,45])# we can add 23, 45 in set so output is {1,2,5,7,8,10,23,45}
print(s)
s.remove('some')#remove() method is used to remove any particuar element
print(s)