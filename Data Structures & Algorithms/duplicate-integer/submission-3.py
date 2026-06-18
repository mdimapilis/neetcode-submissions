class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freqs = {}

        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        for val in freqs.values():
            if val > 1:
                return True

        return False