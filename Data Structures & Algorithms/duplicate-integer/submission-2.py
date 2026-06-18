class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsMap = {}

        for num in nums:
            numsMap[num] = numsMap.get(num, 0) + 1

            if(numsMap[num] >= 2):
                return True
        
        return False
