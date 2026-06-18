class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        #Time: O(n)
        #Space: O(n)
        n = len(cost)
        cache = [0] * (n)
        cache[0], cache[1] = cost[0], cost[1]
        for i in range(2, n):
            cache[i] = cost[i] + min(cache[i - 1], cache[i - 2])
        return min(cache[n - 1], cache[n - 2])



        # def dfs(i):
        #     if i >= n:
        #         return 0
        #     if cache[i] != -1:
        #         return cache[i]
        #     cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
        #     print(cache[i])
        #     return cache[i]
        # return min(dfs(0), dfs(1))

