class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            myMap[n] = 1 + myMap.get(n, 0)
        for n, c in myMap.items():
            freq[c].append(n)
        
        result = []
        for i in range(len(freq)- 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result