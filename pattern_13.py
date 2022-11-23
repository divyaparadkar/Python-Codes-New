#reverse Hill pattern.

n=5
for i in range(n):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i, n):
        print('#', end=' ')
    for i in range(i, n):
        print('#', end=' ')
    print()