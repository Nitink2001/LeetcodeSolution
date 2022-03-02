class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        ans=[]
        res=[]
        candidates.sort()
        def backtrack(i,target):
            
            if target<0:return
            
            if target==0:
                #if ans not in res:   -> this gives TLE
                res.append(ans[:])
                return
            prev=-1
            for j in range(i,len(candidates)):
                
                if candidates[j] == prev:
                    continue
                ans.append(candidates[j])
                
                backtrack(j+1,target-candidates[j])
                
                ans.pop()
                
                prev = candidates[j]

                
        backtrack(0,target)
        return res
                
