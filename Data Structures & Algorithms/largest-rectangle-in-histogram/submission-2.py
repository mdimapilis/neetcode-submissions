class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, maxArea = [], 0

        for i, h in enumerate(heights):
            start = i    
            while stack and h < stack[-1][1]:
                prevI, prevH = stack.pop()
                maxArea = max(maxArea, prevH * (i - prevI))
                start = prevI
                
            stack.append([start, h])

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea


        # n, maxArea = len(heights), 0

        # for i, h in enumerate(heights):

        #     right = i + 1
        #     left = i

        #     while right < n and heights[right] >= h:
        #         right += 1

        #     while left >= 0 and heights[left] >= h:
        #         left -= 1
        #     right -= 1
        #     left += 1
        #     print(i, ' ', h, ' ', right, ' ', left)
        #     maxArea = max(maxArea, h * (right - left + 1))

        # return maxArea