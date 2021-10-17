class Solution:
                            
    def isValidSudoku(self, board):
        # check rows 
        for r in range(9):
            hashSet = set()
            for c in range(9):
                if board[r][c] != ".":
                    if board[r][c] in hashSet:
                        return False
                    else:
                        hashSet.add(board[r][c])
                
        # check columns 
        for r in range(9):
            hashSet = set()
            for c in range(9):
                if board[c][r] != ".":
                    if board[c][r] in hashSet:
                        return False
                    else:
                        hashSet.add(board[c][r])
        # check matrix 3 * 3 
        r, c = 0, 0
        while True:
            hashSet = set()
            for i in range(r, r+3):
                for j in range(c, c + 3):
                    if board[i][j] != ".":
                        if board[i][j] in hashSet:
                            return  False
                        else:
                            hashSet.add(board[i][j])
            c += 3
            if c == 9:
                r += 3
                if r == 9:
                    break
                c = 0
        return True
        
       
board =[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

solve = Solution()
print(solve.isValidSudoku(board))
