def fourNumberSum(array, targetSum):
    result = []
    for i in range(0,len(array) - 3):
        for j in range(i+1,len(array) - 2):
            for k in range(j+1,len(array) - 1):
                for l in range(k+1,len(array)):
                    if array[i] + array[j] + array[k] + array[l] == targetSum:
                        result.append([array[i] , array[j] , array[k] , array[l]])
    
    return result


def fourNumberSum(array, targetSum):
    result = []
    targetValue = 0
    for i in range(0,len(array) - 2):
        for j in range(i+1,len(array) - 1):
            for k in range(j+1,len(array)):
                targetValue = targetSum - (array[i] + array[j] + array[k])
                if targetValue in array:
                    result.append([array[i] , array[j] , array[k] , targetValue])
    
    return result




array = [7,6,4,-1,1,2]
targetSum = 16
print(fourNumberSum(array,targetSum))