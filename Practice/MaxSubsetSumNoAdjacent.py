def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    
    maxSums = array[:]
    maxSums[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        maxSums[i] = max(maxSums [i - 1], maxSums[i - 2] + array[i])
    
    return maxSums[-1]

def maxSubsetSumNoAdjacentopti(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    
    first = array[0]
    second = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(second, first + array[i])
        first = second
        second = current
    return second

 
# Time Complexity - O(n) 
# Space Complexity - O(n)
def maxSubsetSumNoAdjacenta(array):
    if not len(array):
        return 0
    if(len(array) == 1):
        return array[0]

    sumsArray = array[:]
    sumsArray[1] = max(array[0],array[1])
    for i in range(2,len(array)):
        sumsArray[i] = max(sumsArray[i-1],array[i] + sumsArray[i-2])
    return sumsArray[-1]


# OPTIMIZING..
# Time Complexity - O(n)
# Space Complexity - O(1)
def maxSubsetSumNoAdjacentaopti(array):
    if not len(array):
        return 0
    if len(array) == 1:
        return array[0]
    first = array[0]
    second = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(second, first + array[i])
        first = second
        second = current
    return second






array = [75, 105, 120, 75, 90, 135]
print (maxSubsetSumNoAdjacentaopti(array))

