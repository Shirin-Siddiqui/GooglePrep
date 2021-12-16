# Time Complexity - O(n) where n is the length of the array
# Space Complexity - O(1)
def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1
    while(i < j):
        if array[j] == toMove:
            j -= 1
        if array[i] != toMove:
            i += 1
        if array[i] == toMove and array[j] != 2:
            array = swap(array,i,j)
            i += 1
            j -= 1
    return array


def swap(array,i,j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
    return array



# Time Complexity - O(n) where n is the length of the array
# Space Complexity - O(1)
# Same thing but smarter approach
def moveElementToEndnb(array, toMove):
    i = 0
    j = len(array) - 1
    while i < j:
        while i < j and array[j] == toMove:
            j -= 1
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        i += 1
    return array

array = [2,1,2,2,2,3,4,2]
toMove = 2
print(moveElementToEndnb(array,toMove))