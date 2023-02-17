def add(*n):
    s=0
    print(n)
    print(type(n))
    for i in n:
        s=s+i
    print(s)
add(12,23,10,24,56,7)

def run(name, *p):
    add=0
    for i in p:
        add=add+i
    print(name,'=',add)
run('A',23,45,56,34)
run('B',34,45,35,45)
run('C',34,56,68,78)