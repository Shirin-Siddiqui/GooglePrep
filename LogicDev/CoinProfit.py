def maxCoinsProfit(n,coins):
    if n == 0:
        return coins[n]
    return max(coins[n] + maxCoinsProfit(n-1,coins) , maxCoinsProfit(n-1,coins))
    

coins = [0,-1,-1,-1,-1,-1] #[10,10,10,0,-3,0,5]
n = len(coins)-1
print(maxCoinsProfit(n,coins))


1 2 3 4 5
5 4 3 2 1
2 3 4 5 6


1) 1d array
2) 2d array
3) deduct tax



5 + 5 + 6 -4 -4 = 8
3 + 3 + 4 = 10
5 + 1 + 6 = 12














