class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]
            # print(sum)
            # print("l before:", l)
            # print("r before:", r)
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            # print("l after:", l)
            # print("r after:", r)
            else:
               return [l + 1, r + 1] 
        return []