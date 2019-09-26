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
    
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and (balanced == True):
        symbol = symbolString[index]   
        if symbol == "(":              
            s.push(symbol)
        elif (s.isEmpty() == True):     
            balanced == False
        else:                          
            s.pop()
        index += 1                      
        
    if (balanced == True) and (s.isEmpty() == True): 
        return True
    else:
        return False
    
print(parChecker("((()))"))
print(parChecker("(()"))
