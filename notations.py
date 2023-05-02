numbers= [3,6,2,4,5,6,4,8,9]
duplicate= None
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):  #--------n^2 iterations
        if numbers[i] == numbers[j]:
            duplicate = numbers[i]
            break

for i in range(len(numbers)):
    if numbers[i] == duplicate: #-----------n iteration
        print(i)
