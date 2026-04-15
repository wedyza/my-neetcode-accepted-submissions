class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = []
            column = []
            for j in range(9):
                if board[i][j].isdigit():
                    row.append(board[i][j])
                if board[j][i].isdigit():
                    column.append(board[j][i])
            set_column = set(column)
            set_row = set(row)
            if len(row) != len(set_row) or len(column) != len(set_column):
                return False
        
        for i in range(3):
            for j in range(3):
                x = i * 3
                y = j * 3
                l = board[x][y:y+3]
                l += board[x + 1][y:y+3]
                l += board[x + 2][y:y+3]
                
                digits = []
                for s in l:
                    if s.isdigit():
                        digits.append(s)
                
                if len(digits) != len(set(digits)):
                    return False
        return True