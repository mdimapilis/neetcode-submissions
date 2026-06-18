class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n, res = len(nums), set()

        for i in range(n - 1):
            j, k = i + 1, n - 1

            while j < k:
                target, curr = -nums[i], nums[j] + nums[k]

                if curr < target:
                    j += 1
                elif curr > target:
                    k -= 1
                else:
                    res.add(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                    k -= 1

        return list(res)