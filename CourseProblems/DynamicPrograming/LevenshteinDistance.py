'''    PROBLEM STATEMENT - LEVENSHTEIN DISTANCE

Write a function that takes in two strings and returns the minimum number of operations needed to be performed on the first string
in order to obtain the second string

eg - 
str1 = "abc"
str2 = "yabd"
answer = 2

'''

# Time Complexity = O(nm) where n is the length of string 1 and m is the length of string 2
# Space Complexity = O(nm) where n is the length of stirng 1 and m is the length of string 2

def levenshteinDistance(str1, str2):
    edits = [[x for x in range(len(str1)+1)] for y in range(len(str2)+1)]
    for x in range(1,len(str2)+1):
        edits[x][0] = edits[x-1][0] + 1
    for r in range(1,len(str2)+1):
        for c in range(1,len(str1)+1):
            if str2[r-1] == str1[c-1]:
                edits[r][c] = edits[r-1][c-1]
            else:
                edits[r][c] = 1 + min(edits[r-1][c],edits[r][c-1],edits[r-1][c-1])
    return edits

# Time Complexity = O(nm) where n is the length of string 1 and m is the length of string 2
# Space Complexity = O(min(n,m)) the minimum of the length of the 2 values

def levenshteinDistanceOptimized(str1, str2):
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2  
    evenEdits = [x for x in range(len(small) + 1)]
    oddEdits = [None for x in range(len(small) + 1)]
    for i in range(1, len(big) + 1):
        if i % 2 != 0:
            currentEdits = oddEdits
            previousEdits = evenEdits
        else:
            currentEdits = evenEdits
            previousEdits = oddEdits
        currentEdits[0] = i
        for j in range(1, len(small) + 1):
            if big[i-1] == small[j-1]:
                currentEdits[j] = previousEdits[j-1]
            else:
                currentEdits[j] = 1 + min(currentEdits[j-1], previousEdits[j], previousEdits[j-1])
    return currentEdits[-1] #evenEdits[-1] if len(big) % 2 == 0 else oddEdits[-1]
	
str1 = "abc"
str2 = "yabd"
print(levenshteinDistanceOptimized(str1,str2))





