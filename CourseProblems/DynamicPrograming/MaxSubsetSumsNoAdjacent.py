''' PROBLEM STATEMENT - MAX SUBSET SUM NO ADJACENT

Write a function that takes in an array of positive integers and returns the maximum sum of non-adjacent elements in the array
eg : 

1) [7,10,12,7,9,14] = 33
2) [75, 105, 120, 75, 90, 135] = 330

'''

# Time Complexity - O(n) where n is the length of the input array
# Space Complexity - O(n) where n is the length of the input array

def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return
    elif len(array) == 1:
        return array[1]
    maxSums = array[:]
    maxSums[1] = max(array[0],array[1])
    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i-1],maxSums[i-2] + array[i])
    return maxSums[-1]

# Time Complexity - O(n) where n is the length of the input array
# Space Complexity - O(1) 

def maxSubsetSumNoAdjacentOptimized(array):
    if not len(array):
        return
    elif len(array) == 1:
        return array[1]
    second = array[0]
    first = max(array[1],array[0])
    for i in range(2, len(array)):
        current = max(first,second + array[i])
        second = first
        first = current
    return current


array = [75, 105, 120, 75, 90, 135]
print (maxSubsetSumNoAdjacentOptimized(array))
