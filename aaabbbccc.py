s= input('Enter string')
output =''
previous =''
for i in s:
    if i.isalpha():
        output +=i
        previous =i
    else:
        output += previous*(int(i)-1)
    print(output)