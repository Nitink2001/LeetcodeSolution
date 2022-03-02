class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        
        mapper = {2:"abc", 3:"def", 4:"ghi", 5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        ans = set()
        
        def combination(mapper, digits, ans, s, curr):
            if len(digits)==0:return []
            
            if curr>=len(digits):
                ans.add(''.join(s))
                return
            
            val = digits[curr]
            string = mapper[int(val)]
            
            for i in range(len(string)):
                s.append(string[i])
                combination(mapper,digits,ans,s,curr+1)
                s.pop()
        combination(mapper,digits,ans,[],0)
        return ans
            
                
                
