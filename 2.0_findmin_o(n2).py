import time
from random import randrange

def findmin(alist):
    overallmin = alist[0]   
    for i in alist:         
        issmallest = True
        for j in alist:     
            if i > j:
                issmallest = False
        if issmallest == True: 
            overallmin = i
    return overallmin

print(findmin([5,4,2,1,0]))
print(findmin([0,4,2,1,5]))

print("\n")

for listSize in range(1000,10001,1000):                  
    alist = [randrange(10000) for x in range(listSize)]  
    start = time.time()
    print("smallest number: %d" % findmin(alist))        
    end = time.time()
    print("size: %d, time: %f\n" % (listSize, end-start))
