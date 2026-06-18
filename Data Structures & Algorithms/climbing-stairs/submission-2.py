class Solution:
    def climbStairs(self, n: int) -> int:

        
        if (n <= 2):
            return n
        cache = [-1] * (n + 1)
        cache[1], cache[2] = 1, 2
        
        for i in range(3, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]
        
        return cache[n]

        #time: O(2^n)
        #space: O(n)
        # res = 1
        # if(n == 1):
        #     return res
        # if (n == 2):
        #     res += 1
        #     return res
        # res = self.climbStairs(n - 1) + self.climbStairs(n-2)
        # return res