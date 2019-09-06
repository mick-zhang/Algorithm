class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
def divideBy2(decNumber):
    remainderStack = Stack()
    
    while decNumber > 0:                      
        remainder = decNumber % 2
        remainderStack.push(remainder)
        decNumber = decNumber // 2
        
    binaryString = ""
    while remainderStack.isEmpty() == False: 
        binaryString += str(remainderStack.pop())
        
    return binaryString

print(divideBy2(42))
