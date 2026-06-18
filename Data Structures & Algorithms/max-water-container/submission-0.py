class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxHeight = 0

        l, r = 0, len(heights) - 1

        while l < r:
            water = (r - l) * min(heights[l], heights[r])
            maxHeight = max(maxHeight, water)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxHeight


        # brute force
        # maxHeight = 0
        # for i in range(len(heights)):
        #     for j in range(len(heights)):
        #         water = (j - i) * min(heights[i], heights[j])
        #         maxHeight = max(maxHeight, water)
        #         print(water)
        # return maxHeight