class BridgesAdjacencyList:
	def __init__(self,n=None,graph=None,bridges=[]):
		#self.n1=n
		self.n=n
		self.id=0
		self.low=[float('inf')]*(self.n)
		self.ids=[float('inf')]*(self.n)
		self.solved=False
		self.visited=[False]*(self.n)
		self.graph=self.buildGraph(graph)
		self.bridges=[]
		self.arr=[[]*(self.n)]

	def buildGraph(self,graph):
		self.arr=[[]*(self.n)]
		#arr=[[]*(self.n)]
		for i in graph:
			x,y=i[0],i[1]
			#print(x,y)
			arr[x].append(y)
			arr[y].append(x)
		return(arr)

	def bridgesAdjList(graph,n):
		assert(graph!=None)
		assert(n>0)
		assert(len(graph)!=n)
		self.graph=graph
		self.n=n

	"""
	Returns list of pair of nodes that form bridges


	"""
	def findBridges(self):
		if(self.solved):
			return(self.bridges)
		#self.id=0
		#self.low = [float('inf')]*(self.n)
		#self.ids = [float('inf')] * (self.n)
		#self.visited = [False] * (self.n)
		#self.bridges=[]
		for i in range(self.n):
			if(self.visited[i]==False):
				self.dfs(i,-1)
		self.solved = True
		return(self.bridges)

	def dfs(self,at,parent):
		self.visited[at]=True
		self.low[at] = self.ids[at] = self.id
		self.id+=1

		for v in self.graph[at]:
			if(v==parent):
				continue
			if(self.visited[v]==False):
				self.dfs(v,at)
				self.low[at] = min(self.low[at],self.low[v])
				if(self.ids[at]<self.low[v]):
					self.bridges.append([at,v])
			else:
				self.low[at] = min(self.low[at],self.low[v])

arr=	[
			[0,1],
			[0,2],
			[1,2],
			[2,3],
			[3,4],
			[2,5],
			[5,6],
			[6,7],
			[7,8],
			[8,5]
		]
solver = BridgesAdjacencyList(graph=arr,n=9)
bridges = solver.findBridges()
for i in range(len(bridges)//2):
	n1,n2=bridges[2*i],bridges[2*i + 1]
	print("bridges between nodes",n1,"and",n2)

print(bridges)
