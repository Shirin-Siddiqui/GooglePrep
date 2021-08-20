def knapsack(w,val,c,n,memoized):
    if n == 0 or w == 0:
        return 0
    if memoized[n][c] != -1:
        return memoized[n][c]
    
    if w[n-1] <= c:
        memoized[n][c] = max(
            val[n-1] + knapsack(w,val,c - w[n-1],n-1,memoized),
            knapsack(w,val,c,n-1,memoized)
        )
        return memoized[n][c]
    elif w[n-1] > c:
        memoized[n][c] = knapsack(w,val,c,n-1,memoized)
        return memoized[n][c]

w = [10,20,30]
val = [60,100,120]
c = 50

memoized = [[-1 for i in range(c+1)] for j in range(len(w)+1)]
print(knapsack(w,val,c,len(w), memoized))


