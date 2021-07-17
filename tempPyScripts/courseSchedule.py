class Node:
    def __init__(self):
        self.inD = 0
        self.outNodes = []
from collections import defaultdict,deque
class Solution:
    def canFinish(self, numCourses, prereq):
        if(len(prereq)<2):
            return(True)
        edgesCount = 0
        self.g=defaultdict(Node)
        for u,v in prereq:
            edgesCount +=1
            self.g[v].outNodes.append(u)
            self.g[u].inD+=1
        print(self.g)
        zdC = deque()
        for indx,nd in self.g.items():
            print(indx,nd.inD,nd.outNodes)
            if(nd.inD==0):
                zdC.append(indx)
        removedEdges = 0
        while zdC:
            c = zdC.pop()
            for x in self.g[c].outNodes:
                self.g[x].inD -=1
                removedEdges +=1

                if(self.g[x].inD ==0):
                    zdC.append(x)
        if(removedEdges==edgesCount):
            return(True)
        return(False)
s=Solution()
n=6
arr=[[1,0],[2,1],[3,1],[4,3],[5,3]]
print(s.canFinish(n,arr))
