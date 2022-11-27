'''find number between 1000 and 3000 (bothincluded)such that each digits of a number obtanined should be printed in a sequence '''
for j in range(1000, 3001):
    n = j
    even_count = 0
    while (n > 0):
        rem = n % 10
        if (rem % 2 == 0):
            even_count += 1
        n = int(n / 10)
    if(even_count == 4):
        print(j)


