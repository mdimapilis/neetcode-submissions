class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        prefix, suffix = [1] * n, [1] * n
        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1] 

        for i in range(n):
            product = prefix[i] * suffix[i]
            res.append(product)

        return res
            

        # O(n^2)
        # res = [1] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j:
        #             res[i] = res[i] * nums[j]

        # return res