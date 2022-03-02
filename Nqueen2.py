class Solution:
    def totalNQueens(self, n: int) -> int:
        
        col=set()
        posDiag=set()
        negDiag=set()
        self.count=0
        self.maxi=0
        if n==1:
            return 1
        def backtrack(r):
            
            if r==n:
                self.count+=1
                if self.count>self.maxi:    //Max count
                    self.maxi=self.count
                return
            
            
            for c in range(n):
                
                if c in col or (r+c) in posDiag or (r-c) in negDiag:     //check if queen is in same col or daigonal with other queen if yes, skip
                    continue
                
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                
                backtrack(r+1)
                
                col.remove(c)                       //backtrack
                posDiag.remove(r+c)
                negDiag.remove(r-c)
        backtrack(0)
        return self.maxi
