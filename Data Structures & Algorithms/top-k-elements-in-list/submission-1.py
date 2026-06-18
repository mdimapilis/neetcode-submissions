class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        bucket = [[] for i in range(len(nums) + 1)]
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        for key, value in freqs.items():
            bucket[value].append(key)
        res = []
        
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
            if len(res) == k:
                return res