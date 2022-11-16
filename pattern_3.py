#Displaying number from 1 to 100 in 10 rows 10 cols.
for x in range(1, 11):
    for y in range(1, 11):
        print('{:8}'.format(x*y), end='')
    print()