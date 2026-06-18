class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # brute force
        nums.sort()
        n, res = len(nums), set()

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    sum = nums[i] + nums[j] + nums[k]

                    if sum == 0:
                        triplet = [nums[i], nums[j], nums[k]]
                        res.add(tuple(triplet))

        return list(res)