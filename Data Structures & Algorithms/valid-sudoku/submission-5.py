class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows, cols, sqrs = [0] * 9, [0] * 9, [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                val = int(board[r][c]) - 1
                if (1 << val) & rows[r]:
                    return False
                if (1 << val) & cols[c]:
                    return False
                if (1 << val) & sqrs[(r // 3) * 3 + (c // 3)]:
                    return False
                
                rows[r] |= (1 << val)
                cols[c] |= (1 << val)
                sqrs[(r // 3) * 3 + (c // 3)] |= (1 << val)

        return True

        # works, but time O(n^2) and space O(n)
        # check horizontally
        # for row in range(9):
        #     dupes = set()
        #     for col in range(9):
        #         curr = board[row][col]
        #         if curr != '.' and curr in dupes:
        #             return False
        #         dupes.add(curr)
        
        # # check vertically
        # for col in range(9):
        #     dupes = set()
        #     for row in range(9):
        #         curr = board[row][col]
        #         if curr != '.' and curr in dupes:
        #             return False
        #         dupes.add(curr)

        # for box in range(9):
        #     dupes = set()
        #     for row in range(3):
        #         for col in range(3):
        #             currX, currY = (box // 3) * 3 + row, (box % 3) * 3 + col
        #             curr = board[currX][currY]

        #             if curr != '.' and curr in dupes:
        #                 return False
        #             dupes.add(curr)

        # return True