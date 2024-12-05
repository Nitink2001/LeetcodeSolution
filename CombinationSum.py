class Solution:
    #changes for PR bot trigger
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        res=[]
        ans=[]
        def backtrack(i,target):
            
            if target<0:return
            if target==0:
                res.append(ans[:])
                return
            
            for j in range(i,len(candidates)):

                ans.append(candidates[j])
                backtrack(j,target-candidates[j])
                ans.pop()
                
        backtrack(0,target)
        return res
                
                
