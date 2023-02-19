#MAP function 
"""map
map() Function:- This function executes a spacified function on each elements of the iterable (sequence )and paerhaps changes the elements .

synatx:

map(function_name, iterable)

function_name:- It's name of function which perform an operation an all the elements of the sequence and modified elemnts are returned which can be stored in another sequence .

iterable:- it may be either sequence, list, string, tuple, a container which supports iteration, or an iterator."""


l=input().split(',')
l1=input().split(',')
if  len(l)==len(l1):
    def fun(x,y):
        return  int(x)+int(y)
    result=list(map(fun,l,l1))
    print(result)
else:
    print("list")
        