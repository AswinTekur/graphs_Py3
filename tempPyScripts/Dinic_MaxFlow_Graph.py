from collections import defaultdict
class Edge:
    def __init__(self,src=None,to=None,residual=0,flow=0,capacity=0):
        self.src = src
        self.to = to
        self.residual = Edge
        self.flow = flow
        self.capacity = capacity

    def isResidual(self):
        return(self.capacity == 0)

    def remainingCapacity(self):
        return(self.capacity - self.flow)

    def augment(self,bottleNeck):
        self.flow += bottleNeck
        self.residual.flow -= bottleNeck

class NetworkFlowSolverBase:
    def __init__(self,n=None,s=None,t=None):
        self.n=n
        self.s=s
        self.t=t

        #self.solved = False
        self.maxFlow = 0
        #self.graph = defaultdict(list)

        self.graph = self.buildGraph()

        self.LARGE_V = 10000
        self.level = [0]*self.n
        #self.nxt = [0]*self.n

    def buildGraph(self):
        self.arr = []
        for i in range(self.n):
            self.arr.append([])
        return(self.arr)

    def addEdge(self,src,to,capacity):
        e1 = Edge(src,to,capacity=capacity)
        e2 = Edge(to,src,capacity=0)

        e1.residual = e2
        e2.residual = e1

        self.graph[src].append(e1)
        self.graph[to].append(e2)

    def solve(self):
        self.nxt = [0]*self.n

        while(self.bfs()):
            self.nxt = [0]*self.n

            f = 1
            while(f !=0):
                f = self.dfs(self.s, self.nxt, self.LARGE_V)
                self.maxFlow +=f

    def bfs(self):
        self.level = [-1]*self.n
        q = [self.s]
        self.level[self.s]=0

        while(q):
            node = q.pop(0)
            for edge in self.graph[node]:
                cap = edge.remainingCapacity()
                if(cap>0 and self.level[edge.to]== -1):
                    self.level[edge.to] = self.level[node] +1
                    q.append(edge.to)
        return(self.level[self.t]!= -1)

    def dfs(self,at,nxt,flow):
        if(at==self.t):
            return(flow)

        numEdges = len(self.graph[at])


        for i in range(self.nxt[at],numEdges):
            print(at,i)
            edg = self.graph[at][i]
            cap = edg.remainingCapacity()
            if(cap>0 and self.level[edg.to] == self.level[at]+1):
                bottleNeck = self.dfs(edg.to, self.nxt, min(cap,flow))
                print("bottleNeck",bottleNeck)
                if(bottleNeck>0):
                    edg.augment(bottleNeck)
                    return(bottleNeck)


        #for edg in self.graph[at]:
        #    cap = edg.remainingCapacity()
        #    if(cap>0 and self.level[edg.to]==self.level[at]+1):
        #        bottleNeck = self.dfs(edg.to, self.nxt, min(cap,flow))
        #        if(bottleNeck>0):
        #            edg.augment(bottleNeck)
        #            return(bottleNeck)
        return(0)

if __name__ == '__main__':
    n = 11
    s=n-1
    t=n-2
    solver = NetworkFlowSolverBase(n,s,t)

    solver.addEdge(s, 0, 5)
    solver.addEdge(s, 1, 10)
    solver.addEdge(s, 2, 15)

    # Middle edges
    solver.addEdge(0, 3, 10)
    solver.addEdge(1, 0, 15)
    solver.addEdge(1, 4, 20)
    solver.addEdge(2, 5, 25)
    solver.addEdge(3, 4, 25)
    solver.addEdge(3, 6, 10)
    solver.addEdge(4, 2, 5)
    solver.addEdge(4, 7, 30)
    solver.addEdge(5, 7, 20)
    solver.addEdge(5, 8, 10)
    solver.addEdge(7, 8, 15)

    # Sink edges
    solver.addEdge(6, t, 5)
    solver.addEdge(7, t, 15)
    solver.addEdge(8, t, 10)
    solver.solve()

    #print(solver.graph)

    print(solver.maxFlow)
