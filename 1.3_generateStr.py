import random

def generateStr(strlen):     
    result = ""             
    alphabet = "abcdefghijklmnopqrstuvwxyz "  
    for letters in range(strlen):                 
        result += alphabet[random.randrange(27)]
    return result

def score(goalstring, teststring):
    numSame = 0
    for letters in range(len(goalstring)):              
        if goalstring[letters] == teststring[letters]:  
            numSame += 1                                
    return numSame / len(goalstring)                    

def main():
    goalstring = "hello"                                
    newstring = generateStr(5)                          
    newscore = score(goalstring, newstring)             
    
    bestscore = 0                                       
    
    while newscore < 1:
        if newscore > bestscore:
            print(newscore, newstring)
            bestscore = newscore                        
        
        newstring = generateStr(5)                      
        newscore = score(goalstring, newstring)         
        

    if newscore == 1:                                   
        print(newscore, newstring)                      
        
main()
