def doubleLast(j):
    myList = j
    
    myList.append(myList[-1])
    return myList

print(doubleLast([1,2,3,4,5]))

