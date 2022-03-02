class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        for i in range(9):
            for j in range(9):
                
                if board[i][j]==".":
                    
                    for c in ['1','2','3','4','5','6','7','8','9']:
                        
                        if self.isValid(board,i,j,c):
                            
                            board[i][j] = c
                            
                            if self.solveSudoku(board) == True:
                                return True
                            
                            else:
                                board[i][j]='.'   #backtracking
                    return False
        return True
    def isValid(self,board,row,col,c):
        
        for i in range(9):
            if board[row][i] == c: return False
            if board[i][col] == c:return False
            if (board[3*(row//3)+i//3][3*(col//3)+i%3]==c):return False
        return True
                
            
