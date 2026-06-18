class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myMap = {}
        for i in range(len(nums)):
            myMap[nums[i]] = myMap.get(nums[i], 0) + 1

        for key in myMap:
            if myMap[key] >= 2:
                return True
        return False

         