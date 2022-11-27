import numpy as op
arr1 = op.array([[12, 5], [3, 6]])
arr2 = op.array([[23, 7], [4, 6]])
print("Matrix 1 is \n", arr1)
print("Matrix 2 is \n", arr2)
ans = op.multiply(arr1, arr2)
print('The multiplication of array is ',ans)