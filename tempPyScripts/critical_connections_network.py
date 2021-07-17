from collections import defaultdict
class Solution:
    def criticalConnections(self, n, connections):
        self.g=defaultdict(list)
        for i in connections:
            self.g[i[0]].append(i[1])
        self.ids=list(range(n))
        self.visited=[False]*n
        self.id=0
        def dfs(i):
            self.visited[i]=True
            self.ids[i]=self.id
            for v in self.g[i]:
                if(not self.visited[v]):
                    dfs(v)
        for i in range(n):
            if(self.visited[i]==False):
                dfs(i)
                self.id+=1
        print("self ids",self.ids)
        res=[]
        for i in connections:
            k,kx=i[0],i[1]
            if(self.ids[k]!=self.ids[kx]):
                res.append([k,kx])
        return(res)
s=Solution()
arr=[[0,1],[1,2],[2,0],[1,3]]
n=4
print(s.criticalConnections(n,arr))
