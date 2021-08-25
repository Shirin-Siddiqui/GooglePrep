class Solution:
    def _init_(self):
        self.memoized = []
        self.max = 0

    def maxProfit(self, nums):
        self.nums = nums
        return self.maxProfit_dp(0)
    
    def maxProfit_dp(self,n):
        #print(n)
        if n < len(self.nums)-1:
            return max(self.nums[n] - self.maxProfit_dp(n+1), self.maxProfit_dp(n+1))
        elif n == len(self.nums)-1:
            return self.nums[n]
        else:
            return 0
        
if __name__ == '__main__':

    nums = [7,1,5,3,6,4] #[183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]

    sol = Solution()
   # sol.memoized = [-1 for i in range(len(nums)+1) ]

    print(sol.maxProfit(nums))