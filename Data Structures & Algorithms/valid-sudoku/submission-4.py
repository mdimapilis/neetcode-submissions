class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check horizontally
        for row in range(9):
            dupes = set()
            for col in range(9):
                curr = board[row][col]
                if curr != '.' and curr in dupes:
                    return False
                dupes.add(curr)
        
        # check vertically
        for col in range(9):
            dupes = set()
            for row in range(9):
                curr = board[row][col]
                if curr != '.' and curr in dupes:
                    return False
                dupes.add(curr)

        for box in range(9):
            dupes = set()
            for row in range(3):
                for col in range(3):
                    currX, currY = (box // 3) * 3 + row, (box % 3) * 3 + col
                    curr = board[currX][currY]

                    if curr != '.' and curr in dupes:
                        return False
                    dupes.add(curr)

        return True