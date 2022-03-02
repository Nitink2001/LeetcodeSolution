class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        
        ans=set()
        def backtrack(o,c,s):
            if o==c==n:
                ans.add(''.join(s))
                return
            if o<n:
                s.append("(")
                backtrack(o+1,c,s)
                s.pop()
            if c<o:
                s.append(")")
                backtrack(o,c+1,s)
                s.pop()
        backtrack(0,0,[])
        return ans
                
