class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        print(ROWS, ' ', COLS)
        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            row, col = m // COLS, m % COLS
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False



        # m, n = len(matrix) - 1, len(matrix[0]) - 1
        # top, l = 0, 0
        # bottom, r = m, n
        
        # while top <= bottom: #perform binary search on rows to see if target in row range
        #     midR = (top + bottom) // 2
        #     if matrix[midR][0] > target:
        #         bottom = midR - 1
        #     elif target > matrix[midR][n]:
        #         top = midR + 1
        #     else:
        #         break

        # while l <= r: #perform binary search on columns and identified row
        #     midR = (top + bottom) // 2
        #     midC = (l + r) // 2

        #     if matrix[midR][midC] == target:
        #         return True
        #     elif matrix[midR][midC] > target:
        #         r = midC - 1
        #     else:
        #         l = midC + 1

        # return False