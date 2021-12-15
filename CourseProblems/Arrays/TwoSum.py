'''
Problem is ->

Find a pair which would add up to a target sum ! 

Test Cases - 

[1,2,3,9]   Target Sum = 8  OUTPUT - No
[1,2,4,4]   Target Sum = 8  OUTPUT - Yes
'''

def binarySearch (arr,l,r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return False

# Solution Number 1 -> It has Quadratic Time Complexity O(n^2)

def checkSumQuadratic(a,targetSum):
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            summ = a[i] + a[j]
            if summ == targetSum:
                print("Fount it !")
                return
    print("Couldn't find it !")

# Solution Number 2 -> It has O(nlog(n)) Time Complexity

def checkSumnLogn(a,targetSum):
    for i in range(0,len(a)):
        checkval = targetSum - a[i]
        arr = []
        arr.extend(a)
        arr.remove(a[i])
        if binarySearch(arr,0,len(arr)-1, checkval):
            print("Found it !")
            return
    print("Coundn't find it!")

# Solution Number 3 -> It has O(n) Time Complexity --> Linear!

def checkSumLinear(a,targetSum):
    l = 0
    r = len(a)-1
    while r > l:
        if a[l] + a[r] < targetSum:
            l += 1
        elif a[l] + a[r] > targetSum:
            r -= 1
        else:
            print ("Found it !")
            return
    print("Couldn't find it!")


def dp(a,n,targetSum,memoized):

    if targetSum == 0:
        return True
    if n == 0:
        return False

    if memoized[n-1][targetSum] != -1:
        return memoized[n-1][targetSum]
    
    if a[n-1] > targetSum:
        memoized[n-1][targetSum] = dp(a,n-1, targetSum, memoized)
        return memoized[n][targetSum]

    memoized[n-1][targetSum] = dp(a,n-1, targetSum,memoized)
    return memoized[n-1][targetSum] or dp(a, n-1, targetSum - a[n-1],memoized)
    

a = [1,2,3,9]
targetSum = 8
memoized = [[-1 for i in range(targetSum + 1)] for j in range(len(a)+1)]
print(dp(a,len(a), targetSum, memoized))

#checkSumLinear(a,targetSum)

