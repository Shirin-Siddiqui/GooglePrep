def numberOfWaysToTraverseGraph(width,height):
    ways = [[1 for x in range(width)] for y in range(height)]
    for r in range(1, width):
        for c in range(1, height):
            ways[r][c] = ways[r][c-1] + ways[r-1][c] 
    return ways[-1][-1]

def numberOfWaysToTraverseGraphOptimalSpace(width,height):
    small = width if width < height else height
    big = width if width >= height else height 
    evenEdits = [1 for x in range(small)]
    oddEdits = [None for x in range(small)]
    for i in range(1, big):
        if i % 2 != 0:
            currentEdits = oddEdits
            previousEdits = evenEdits
        else:
            currentEdits = evenEdits
            previousEdits = oddEdits
        currentEdits[0] = 1
        for j in range(1, small):
            currentEdits[j] = currentEdits[j-1] + previousEdits[j]
    return currentEdits[-1]

def numberOfWaysToTraverseGraphMostOptimal(width,height):
    return int(factorial((width -1 ) + (height - 1)) / (factorial(width - 1) * factorial(height - 1)))

def factorial(num):
    result = 1
    for i in range(2,num + 1):
        result *= i
    return result

width = 3
height = 4
print(numberOfWaysToTraverseGraphMostOptimal(width,height))