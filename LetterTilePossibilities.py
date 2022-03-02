seen = set()
        ans = set()
        
        def backtrack(tiles, seen, ans, curr):
            
            if curr!='' and curr not in ans:
                
                ans.add(curr)
            
            for i in range(len(tiles)):
                
                if i not in seen:
                    
                    seen.add(i)
                    backtrack(tiles,seen,ans,curr+tiles[i])
                    seen.remove(i)
        backtrack(tiles,seen,ans,'')
        
        print(ans)
        return len(ans)
