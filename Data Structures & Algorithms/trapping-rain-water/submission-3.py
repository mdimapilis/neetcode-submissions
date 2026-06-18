class Solution:
    def trap(self, height: List[int]) -> int:
        
        total = 0

        for i in range(1, len(height) - 1):
            l, r = 0, len(height) - 1
            heightL = 0
            heightR = 0
            while l < i:
                heightL = max(heightL, height[l])
                l += 1
            while r > i:
                heightR = max(heightR, height[r])
                r -= 1
            curr = min(heightL, heightR) - height[i]
            if curr > 0:
                total += curr

        return total