from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = defaultdict(list)

        for i in range(len(nums)):
            myMap[nums[i]].append(i)
        
        for i in range(len(nums)):
            num = target - nums[i]
            if num in myMap.keys():
                for j in range(len(myMap.get(num))):
                    if i != myMap.get(num)[j]:
                        return [i, myMap.get(num)[j]]
