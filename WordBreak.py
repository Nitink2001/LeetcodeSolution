class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        res=[]
        def dfs(i,string):

            if i==len(s):
                res.append(string[:-1])
                return 
            for j in range(i,len(s)):
                
                cur=s[i:j+1]
                if cur in wordDict:
                    
                    dfs(j+1,string+cur+' ')
                        
                
        dfs(0,'')
        return res
