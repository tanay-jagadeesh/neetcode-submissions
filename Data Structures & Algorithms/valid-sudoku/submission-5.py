class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #Rows
        for r in range(9):
            seen = set()
            for c in range(9):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in seen:
                    return False
                seen.add(board[r][c])

        #Columns
        for c in range(9):
            seen = set()
            for r in range(9):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in seen:
                    return False
                seen.add(board[r][c])
        
        #3by3Matrix
        for boxRow in range(3):
            for boxCol in range(3):
                seen = set()
                for r in range(3):
                    for c in range(3):
                        val = board[boxRow*3 + c][boxCol*3 + r]
                        if val == ".":
                            continue
                        if val in seen:
                            return False
                        seen.add(val)
        return True