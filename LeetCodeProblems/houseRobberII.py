class Solution:
    def rob(self, nums) -> int:
        self.nums = nums
        if len(self.nums) == 1:
            return self.nums[0]
        self.dp1 = [-1 for i in range(len(self.nums))]
        self.dp2 = [-1 for i in range(len(self.nums))]
        val2 = self.robDp(0,len(self.nums)-1,self.dp2)
        val1 = self.robDp(1,len(self.nums),self.dp1)
        return max(val1,val2)
        
    def robDp(self,start,end,dp):
        if start < end - 1:
            if dp[start] != -1: 
                return dp[start]
            dp[start] = max(self.nums[start] + self.robDp(start+2,end,dp), self.robDp(start+1,end,dp))
            return dp[start]
        elif start == end - 1:
            return self.nums[start]
        else:
            return 0

if __name__ == '__main__':
    nums = [1,2,1,1]
    sol = Solution()
   # sol.memoized = [-1 for i in range(len(nums)+1) ]
    print(sol.rob(nums))