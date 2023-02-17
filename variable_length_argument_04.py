def val(**p):
    print("total and average of numbers ")
    for key,value in p.items():
      add=0
      for i in value:
        l=len(value)
        add+=i
    avg=add/l
    print(add)
    print(avg)
val(t1=(10,15,16,19,25,27,28))