def anagramSolution1(s1,s2):
    stillOK = True    
    if len(s1) != len(s2):
        stillOK = False
        
    s1 = s1.lower()
    s2 = s2.lower()
    
    alist = list(s2)       
    pos1 = 0
    
    while pos1 < len(s1) and (stillOK==True): 
        pos2 = 0           
        found = False
        while pos2 < len(alist) and (found == False):
            if s1[pos1] == alist[pos2]:  
                found = True             
            else:                        
                pos2 += 1
                
        if (found == True):
            alist[pos2] = None  
        else:
            stillOK = False
            
        pos1 += 1               
        
    return stillOK              

print(anagramSolution1('Jane', 'Jean'))
