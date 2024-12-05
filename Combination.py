class Solution:
    #comment for PR check automation tool
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        res=[]
        ans=[]
        
        def backtrack(i):
            
                
            if len(ans)==k:
                res.append(ans[:])
                return
            
            for j in range(i,n+1):
                
                ans.append(j)
                backtrack(j+1)
                ans.pop()
        backtrack(1)
        
        return res
