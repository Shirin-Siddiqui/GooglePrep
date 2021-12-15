'''
PROBLEM STATEMENT - SORTED SQUARED ARRAY
'''

# O(n) - Time Complexity where n is the length of the array
# O(n) - Space Complexity where n is the length of the array
def sortedSquaredArray(array):
    square_array = []
    for i in array:
        square_array.append(i*i)
    return sorted(square_array)

