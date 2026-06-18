class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m, n = len(matrix) - 1, len(matrix[0]) - 1
        # print(m, ' ', n)
        lR, lC = 0, 0
        rR, rC = m, n
        
        while lR <= rR:
            midR = (rR + lR) // 2
            if matrix[midR][0] > target:
                rR = midR - 1
            elif target > matrix[midR][n]:
                lR = midR + 1
            else:
                break

        while lC <= rC:
            midR = (rR + lR) // 2
            midC = (rC + lC) // 2

            if matrix[midR][midC] == target:
                return True
            elif matrix[midR][midC] > target:
                rC = midC - 1
            else:
                lC = midC + 1

        return False