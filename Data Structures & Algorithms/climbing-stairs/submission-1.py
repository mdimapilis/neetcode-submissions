class Solution:
    def climbStairs(self, n: int) -> int:

        # cache = [0] * n
        # res = 0
        # def dp(cache, n):
        #     if(cache[n] > 0):
        #         return cache[n]
            

        # for i in range(n):
        #     res += dp(cache, i)

        # return res

        #time: O(2^n)
        #space: O(n)
        res = 1
        if(n == 1):
            return res
        if (n == 2):
            res += 1
            return res
        res = self.climbStairs(n - 1) + self.climbStairs(n-2)
        return res