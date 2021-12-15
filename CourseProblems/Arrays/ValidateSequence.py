'''
PROBLEM STATEMENT - VALIDATE SUBSEQUENCE

'''

# O(n) - Time Complexity where n is the length of the array
# O(1) - Space Complexity
def isValidSubsequence(array, sequence):	
    ap = 0
    sp = 0
    while sp < len(sequence) and ap < len(array):
        if sequence[sp] == array[ap]:
            sp += 1
            ap += 1
        else:
            ap += 1
    if sp == len(sequence):
        return True
    else:
        return False


# O(n) - Time Complexity where n is the length of the array
# O(1) - Space Complexity
# (Same Solution as above, Removed extra lines)
def isValidSequencenb(array, sequence):
    ap, sp = 0
    while ap < len(array) and sp < len(sequence):
        if sequence[sp] == array[ap]:
            sp += 1
        ap += 1
    return sp == len(sequence)


# O(n) - Time Complexity where n is the length of the array
# O(1) - Space Complexity
# (Same Solution, Different Approach)
def isValidSequences2(array, sequence):
    i_seq = 0
    for number in array:
        if i_seq == len(sequence):
            break
        if sequence[i_seq] == number:
            i_seq += 1
    
    return i_seq == len(sequence)


array = [1,1,1,1,1,1]
sequence = [1,1,1]
print(isValidSequences2(array,sequence))
    

    

