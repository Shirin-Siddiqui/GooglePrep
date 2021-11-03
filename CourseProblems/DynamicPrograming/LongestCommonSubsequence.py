def longestCommonSubsequence(str1, str2):
    sequence = []
    for i in range(len(str2)):
        for j in range(len(str1)):
            if str1[j] == str2[i] and str1[j] not in sequence and i < j:
                sequence.append(str1[j])
                break
    
    return sequence

str1 = "ZXVVYZW"
str2 = "XKYKZPW"
print(longestCommonSubsequence(str1,str2))
