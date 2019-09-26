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
        return self.items[-1]  #last index
    
    def size(self):
        return len(self.items)
    
def infixToPostfix(infixexpr):
    prec = {}  
    prec["^"] = 4
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()   
    
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":  
            postfixList.append(token)        
        elif token == '(':                   
            opStack.push(token)               
        elif token == ')':                   
            topToken = opStack.pop()          
            while topToken != '(':            
                postfixList.append(topToken)  
                topToken = opStack.pop()
        else:
            while (opStack.isEmpty() == False) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)                 
    while (opStack.isEmpty() == False):   
        postfixList.append(opStack.pop()) 
    return " ".join(postfixList)         

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infixToPostfix("( A + B ) * ( C + D )"))
print(infixToPostfix("( A + B ) * C"))
print(infixToPostfix("A + B * C"))
