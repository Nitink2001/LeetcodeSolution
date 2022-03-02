n=len(graph)-1
        res=[]
        def dfs(node,ans):
            
            ans.append(node)
            
            if node==n:
                res.append(ans)
                return
            
            for g in graph[node]:
                
                dfs(g,list(ans))
        dfs(0,[])
        return res
