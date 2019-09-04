def anagramSolution4(s1,s2):
    c1 = [0]*26      
    c2 = [0]*26
    
    s1 = s1.lower()
    s2 = s2.lower()
    
    for i in range(len(s1)):             
        pos = ord(s1[i]) - ord('a')    
        c1[pos] += 1                     
        
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1
        
    j = 0
    stillOK = True
    while j < 26 and (stillOK == True): 
        if c1[j] == c2[j]:              
            j += 1
        else:                           
            stillOK = False
            
    return stillOK

print(anagramSolution4('Jane', 'Jean'))
