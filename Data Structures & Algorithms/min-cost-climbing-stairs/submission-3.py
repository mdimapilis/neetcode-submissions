class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        #bottom up space optimized
        if(len(cost) == 2):
            return min(cost[0], cost[1])
        
        prev1 = cost[0]
        prev2 = cost[1]

        curr = 0

        for i in range(2, len(cost)):
            curr = cost[i] + min(prev1, prev2)
            prev1 = prev2
            prev2 = curr
        return min(curr, prev1)

        #Time: O(n)
        #Space: O(n)
        #bottom up
        # n = len(cost)
        # cache = [0] * (n)
        # cache[0], cache[1] = cost[0], cost[1]
        # for i in range(2, n):
        #     cache[i] = cost[i] + min(cache[i - 1], cache[i - 2])
        # return min(cache[n - 1], cache[n - 2])


        #top down
        # def dfs(i):
        #     if i >= n:
        #         return 0
        #     if cache[i] != -1:
        #         return cache[i]
        #     cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
        #     print(cache[i])
        #     return cache[i]
        # return min(dfs(0), dfs(1))

