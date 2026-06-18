class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m, n = len(matrix) - 1, len(matrix[0]) - 1
        top, l = 0, 0
        bottom, r = m, n
        
        while top <= bottom:
            midR = (top + bottom) // 2
            if matrix[midR][0] > target:
                bottom = midR - 1
            elif target > matrix[midR][n]:
                top = midR + 1
            else:
                break

        while l <= r:
            midR = (top + bottom) // 2
            midC = (l + r) // 2

            if matrix[midR][midC] == target:
                return True
            elif matrix[midR][midC] > target:
                r = midC - 1
            else:
                l = midC + 1

        return False