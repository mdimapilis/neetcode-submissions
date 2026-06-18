class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result, stack = [0] * n, [] # pair: [temp, index]
        
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIdx = stack.pop()
                result[stackIdx] = (i - stackIdx)

            stack.append([temp, i])

        return result