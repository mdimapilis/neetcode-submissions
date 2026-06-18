class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #bottom up
        n = len(nums)
        dp = [0] * (n + 2)
        for i in range(2, n + 2):
            dp[i] = max(nums[i - 2] + dp[i - 2], dp[i -1])
        return dp[n + 1]

        #top down
        #time: O(n)
        #space: O(n)
        # cache = [-1] * len(nums)
        # def dfs(i):
        #     if (i >= len(nums)):
        #         return 0
        #     if cache[i] != -1:
        #         return cache[i]
        #     cache[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
        #     return cache[i]
        # return dfs(0)
        
        # brute force: time: O(2^n)
        #way too slow
        # def dfs(i):
        #     if(i >= len(nums)):
        #         return 0
        #     return max(nums[i] + dfs(i + 2), dfs(i + 1))

        # return dfs(0)