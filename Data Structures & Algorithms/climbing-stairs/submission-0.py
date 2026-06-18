class Solution:
    def climbStairs(self, n: int) -> int:
        res = 1
        if(n == 1):
            return res
        if (n == 2):
            res += 1
            return res
        res = self.climbStairs(n - 1) + self.climbStairs(n-2)
        return res