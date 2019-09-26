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
    
def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"              
    
    remainderStack = Stack()
    
    while decNumber > 0:                     
        remainder = decNumber % base          
        remainderStack.push(remainder) 
        decNumber = decNumber // base
        
    binaryString = ""
    while remainderStack.isEmpty() == False:  
        binaryString += digits[remainderStack.pop()] 
        
    return binaryString

print(baseConverter(25,2))
print(baseConverter(233,8))
print(baseConverter(233,16))
