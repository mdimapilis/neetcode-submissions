class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ## BRUTE FORCE

        #iterate through rows, assign a set, if current idx
        #in set then return False b/c already existing in row
        #otherwise add to set
        #iterate rows
        for row in range(9):
            elements = set()
            #iterate in each row
            for i in range(9):
                #blank
                if board[row][i] == ".":
                    continue
                if board[row][i] in elements:
                    return False
                elements.add(board[row][i])
        
        #do the same for cols
        for col in range(9):
            elements = set()

            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in elements:
                    return False
                elements.add(board[i][col])

        #search within 3x3 boxes
        for square in range(9):
            elements = set()

            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j

                    if board[row][col] == ".":
                        continue
                    if board[row][col] in elements:
                        return False
                    elements.add(board[row][col])
        return True