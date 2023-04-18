class Stack:
    def __init_(self):
        self.list =[]

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    #is empty

    def isEmpty(self):
        if self.list ==[]:
            return True
        else:
            return False
        
    # push

    def push(self,value):
        self.list.append(value)
        return"The elementhas been successfully insterted"
        
CustomStack = Stack()
print(CustomStack.isEmpty())
