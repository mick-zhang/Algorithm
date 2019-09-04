import time
from random import randrange

def findmin(alist):
    minsofar = alist[0]
    for i in alist:
        if i < minsofar:
            minsofar = i
    return minsofar

print(findmin([5,4,2,1,0]))
print(findmin([0,4,2,1,5]))

print("\n")

for listSize in range(1000,10001,1000):
    alist = [randrange(10000) for x in range(listSize)]
    start = time.time()
    print("smallest number: %d" % findmin(alist))
    end = time.time()
    print("size: %d, time: %f\n" % (listSize, end-start))
