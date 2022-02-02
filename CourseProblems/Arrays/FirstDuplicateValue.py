# O(n) - Time Complexity where n is the length of the array
# O(n) - Space Complexity where n is the length of the array
def firstDuplicateValue(array):
    setArray = set()
    for i in range(len(array)):
        setArray.add(array[i])
        if len(setArray) != i+1:
            return array[i]
    return -1

# O(n) - Time Complexity where n is the length of the array
# O(1) - Space Complexity
def firstDuplicateValue(array):
    for value in array:
        absVal  = abs(value)
        if array[absVal - 1] < 0:
            return absVal
        array[absVal - 1] *= -1
    return -1