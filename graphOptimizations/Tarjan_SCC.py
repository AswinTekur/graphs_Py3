from collections import defaultdict
class scc_tarjan:
    def __init__(self,n=None,graph=None):
        self.n=n
        self.solved = False
        self.visited = [False]*(self.n)
        self.componentCount = 0
        self.components = [0]*(self.n)
        #self.arr=defaultdict(list)
        self.arr=self.buildGraph(graph)
        self.comp=defaultdict(list)

    def addEdge(self,x,y):
        #print(self.arr)
        #print(x)
        self.arr[x].append(y)
        self.arr[y].append(x)
        #print(self.arr)

    def getComponents(self):
        #self.solve()
        if(not self.solved):
            self.solve()
            #return(self.components)
        #self.solve()
        #return(self.components)
        return(self.comp.values())

    def countComponents(self):
        if(not self.solved):
            self.solve()
        return(self.componentCount)

    def solve(self):
        if(self.solved):
            return()
        for i in range(self.n):
            if(self.visited[i]==False):
                self.componentCount+=1
                self.dfs(i)
        self.solved = True

    def dfs(self,at):
        self.visited[at]=True
        #self.components[at]=self.componentCount
        #self.comp[at].append(self.componentCount)
        self.comp[self.componentCount].append(at)
        for v in self.arr[at]:
            if(self.visited[v]==False):
                self.dfs(v)

    def buildGraph(self,graph):
        #self.arr=[[]*(self.n)]
        self.arr=defaultdict(list)
        #print(self.arr)
        for i in graph:
            x,y=i[0],i[1]
            #print(x,y)
            #print(x,y)
            self.arr[x].append(y)
            self.arr[y].append(x)
            #print(arr)
        return(self.arr)

arr=        [
                [0,1],
                [1,7],
                [7,0],
                [2,5],
                [4,8],
                [3,6],
                [6,9]
            ]
n=11
solver = scc_tarjan(n=n,graph=arr)
print("number of components:",solver.countComponents())
c=solver.getComponents()
#for i in range(n):
#    print("node",i,"is part of component",solver.components[i])
print(solver.countComponents())
print(solver.getComponents())
