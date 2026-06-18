class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #time: O(n*2^n)
        #brute force, but most efficient: backtracking

        result = []

        subset = []
        #[1,2,3]
        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            #decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            #decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return result