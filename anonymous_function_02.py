# Anonymous function with the the help of if else condition
print((lambda n1,n2,n3: n1 if(n1>n2  and n1>n3) else n2 if(n2>n1 and n2>n3)else n3)( int(input()), int(input()),int(input())))