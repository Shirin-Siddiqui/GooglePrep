def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    i=0
    j=0
    sa = []
    sd = abs(arrayOne[0] - arrayTwo[0])
    while i < len(arrayOne) and j < len(arrayTwo):
        csd = abs(arrayOne[i] - arrayTwo[j])
        if csd < sd:
            sd = csd
            sa = [arrayOne[i], arrayTwo[j]]
        if csd == 0:
            return sa
        elif arrayOne[i] < arrayTwo[j]:
            i += 1
        elif arrayOne[i] > arrayTwo[j]:
            j += 1
    return sa

arrayOne = [-1,5,10,20,28,3]
arrayTwo = [26,134,135,15,17]
print(smallestDifference(arrayOne,arrayTwo))


        
        
        

