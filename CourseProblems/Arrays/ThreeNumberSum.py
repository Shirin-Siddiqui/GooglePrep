'''
PROBLEM STATEMENT - THREE NUMBER SUM
'''

# O(n^2) - Time Complexity where n is the length of the array
# O(n) - Space Complexity where n is the length of the array
def threeNumberSum(array, targetSum):
    array.sort()
    threeSumArray = []
    for i in range( len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                threeSumArray.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    
    return threeSumArray

array = [12,3,1,2,-6,5,-8,6]
targetSum = 0
print(threeNumberSum(array,targetSum))

