def minNumberOfCoinsForChange(n, denoms):
    nums = [float('inf') for amount in range(n+1)]
    nums[0] = 0
    for denom in denoms:
        for amount in range(1,n+1):
            if denom <= amount:
                nums[amount] = min(nums[amount], 1+ nums[amount - denom])
    if nums[-1] != float('inf') : return nums[-1]
    else : return -1

denoms = [1,2,4]
n = 6
print(minNumberOfCoinsForChange(n,denoms))