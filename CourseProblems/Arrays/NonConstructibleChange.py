'''
PROBOLEM STATEMENT - NON CONSTRUCTIBLE CHANGE
'''

# O(n) - Time Complexity where n is the number of coins
# O(1) - Space Complexity 
def nonConstructibleChange(coins):
    if len(coins) == 0:
        return 1
    if len(coins) == 1:
        if coins[0] == 1:
            return 2
        else: return 1
    coins.sort()
    minChange = coins[0]
    for i in range(1,len(coins)):
        if coins[i] - minChange == 1:
            minChange += coins[i]
        else:
            return minChange + 1 
    return minChange + 1 

coins = [5, 7, 1, 1, 2, 3, 22]
print(nonConstructibleChange(coins))