# O(n) - Time Complexity where n is the length of the array
# O(1) - Space Complexity
def isMonotonic(array):
    decBool = False
    j = 1
    if len(array) == 0 or len(array) == 1:
        return True
    while(array[j] == array[0]): j += 1
    if array[0] > array[j]: decBool = True
    for i in range(0, len(array) - 1):
        if decBool == True:
            if array[i] < array[i + 1]:
                return False
        else:
            if array[i] > array[i + 1]:
                return False
    return True

array = [-1,-5,-10,-1100,-1100,-1102,-9001]
print(isMonotonic(array))
