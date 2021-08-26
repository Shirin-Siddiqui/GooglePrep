class Solution:
    def __init__(self):
        self.memoized = {}
        
    def minCostClimbingStairs(self, cost) :
        self.cost = cost
        n = len(cost)
        return min(self.minCostClimbingStairsdp( n-1), self.minCostClimbingStairsdp( n-2))
    
    def minCostClimbingStairsdp(self,n):
        if n == 0:
            self.memoized[n] =  self.cost[0]
        if n == 1:
            self.memoized[n] = self.cost[1]

        if n not in self.memoized.keys():
            self.memoized[n] = self.cost[n] + min(self.minCostClimbingStairsdp(n-1),self.minCostClimbingStairsdp(n-2))
        return self.memoized[n]
    
        
        
        
if __name__ == '__main__':

    nums = [1,100,1,1,1,100,1,1,100,1]

    sol = Solution()
   # sol.memoized = [-1 for i in range(len(nums)+1) ]

    print(sol.minCostClimbingStairs(nums))