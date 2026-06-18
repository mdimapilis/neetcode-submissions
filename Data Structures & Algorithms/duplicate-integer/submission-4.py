class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i != j:
                    return True

        return False
            
        # freqs = {}

        # for num in nums:
        #     freqs[num] = freqs.get(num, 0) + 1

        # for val in freqs.values():
        #     if val > 1:
        #         return True

        # return False