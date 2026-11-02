class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        ngang = [[] for _ in range(9)]
        doc = [[] for _ in range(9)]
        o = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] !="." : 
                    ngang[i].append(board[i][j])
        for i in range(9):
            for j in range(9):
                if board[j][i] !=".": 
                    doc[i].append(board[j][i])
        lngang=3
        ldoc=3
        tmp=0
        for i in range(9):
            lngang=3
            for j in range(9):
                if j >= lngang:
                    lngang+=3
                if i >=ldoc:
                    ldoc+=3
                if board[i][j] !="." : 
                    tmp= lngang//3 + ldoc-4
                    o[tmp].append(board[i][j])
        for i in range(9):
            if len(ngang[i]) != len(set(ngang[i])) or len(doc[i]) != len(set(doc[i])) or len(o[i]) != len(set(o[i])):
                return False
        return True