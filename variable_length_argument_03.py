# dictonary in py(**)
def f1(**n):
    print("person info")
    for key, value in n.items():
        print(key,"-",value)
f1(name='divya', age=19,rollno=11)
f1(name='Abhi')

