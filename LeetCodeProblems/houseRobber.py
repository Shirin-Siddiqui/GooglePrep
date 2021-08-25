# Recursion + Memoized solution

class SolutionN:
    def rob(self, nums):
        self.nums = nums
        self.dp = [-1 for i in range(len(nums))]
        return self.robDp(0)
        
    def robDp(self,n):
        print(n)
        if n < len(self.nums)-1:
            if self.dp[n] != -1: 
                return self.dp[n]
            self.dp[n] = max(self.nums[n] + self.robDp(n+2), self.robDp(n+1))
            return self.dp[n]
        elif n == len(self.nums)-1:
            return self.nums[n]
        else:
            return 0

# Iterative Solution

class Solution:
    def rob(self, nums) :
        n = len(nums)
        if(n==0):
            return 0
        
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1,n):
            if(i==1):
                dp[i] = max(nums[0],nums[1])
            else:
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            
        return dp[-1]

# Without Maintaining length, changing nums array

class Solution:

    def _init_(self):
        self.memoized = []
        self.max = 0

    def rob(self, nums) :

        if len(nums) == 0:
            return 0

        if self.memoized[len(nums)] != -1:
            return(self.memoized[len(nums)])

        else:
            self.max = max(nums[0] + self.rob(nums[2:len(nums)]) , self.rob(nums[1:len(nums)]))
            self.memoized[len(nums)] = self.max
            return(self.memoized[len(nums)])



if __name__ == '__main__':

    nums = [1,2,3,1] #[183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]


    sol = SolutionN()
   # sol.memoized = [-1 for i in range(len(nums)+1) ]

    print(sol.rob(nums))