class Solution:
    def trap(self, height: List[int]) -> int:

        # 2 pointers
        l, r = 0, len(height) - 1
        total = 0
        leftMax, rightMax = height[l], height[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(height[l], leftMax)
                total += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(height[r], rightMax)
                total += rightMax - height[r]

        return total
        
        # total, n = 0, len(height)
        # prefix, suffix = [0] * n, [0] * n
        # prefix[0], suffix[n-1] = height[0], height[n-1]
        # for i in range(1, n):
        #     prefix[i] = max(prefix[i-1], height[i])
        # for i in range(n-2, -1, -1):
        #     suffix[i] = max(suffix[i + 1], height[i])

        # for i in range(n):
        #     total += min(prefix[i], suffix[i]) - height[i]

        # return total


        # for i in range(1, len(height) - 1):
        #     l, r = 0, len(height) - 1
        #     heightL = 0
        #     heightR = 0
        #     while l < i:
        #         heightL = max(heightL, height[l])
        #         l += 1
        #     while r > i:
        #         heightR = max(heightR, height[r])
        #         r -= 1
        #     curr = min(heightL, heightR) - height[i]
        #     if curr > 0:
        #         total += curr

        # return total