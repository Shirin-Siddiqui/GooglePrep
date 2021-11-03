'''   PROBLEM STATEMENT - MAXIMUM SUM INCREASING SUBSEQUENCE

Write a function that takes in a non-empty ray of integers and returns the greatest sum that can be generated from a strictly increasing
subsequence in the array as well as n array of numbersn that subsequence

A sequence of an array is a set of numbers that arent necessarily adjacent in the array but are in the same order as they appear
in the array

Example - 

1) array = [10, 70, 20, 30, 50, 11, 30]
OUTPUT = [110, [10, 20, 30, 50]]

2) array = [8, 12, 2, 3, 15, 5, 7]
OUTPUT = [35, [8,12,15]]

'''

# Time Complexity = O(n^2)
# Space Complexity = O(n)
def maxSumIncreasingSubsequence(array):
    sequence = [None for x in array]
    sums = [num for num in array]
    maxSumId = 0
    for i in range(len(array)):
        currentNum = array[i]
        for j in range(0,i):
            otherNum = array[j]
            if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
                sums[i] = sums[j]+ currentNum
                sequence[i] = j
        if sums[i] >= sums[maxSumId]:
            maxSumId = i
    return [sums[maxSumId], buildSequence(array, sequence, maxSumId)]

def buildSequence(array, sequence ,currentId):
    sequenc = []
    while currentId is not None:
        sequenc.append(array[currentId])
        currentId = sequence[currentId]
    return list(reversed(sequenc))



array = [8,12,2,3,15,5,7]
print(maxSumIncreasingSubsequence(array))