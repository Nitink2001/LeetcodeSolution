class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        
        def isPalin(curr):
            
            if curr == curr[::-1]:
                return True
        
        res=[]
        ans=[]
        def backtrack(i):
            
            if i>=len(s):
                
                res.append(ans[:])
                return
            
            for j in range(i,len(s)):
                
                curr = s[i:j+1]
                
                if isPalin(curr):
                    
                    ans.append(curr)
                    backtrack(j+1)
                    ans.pop()
                
        backtrack(0)
        return res
        
