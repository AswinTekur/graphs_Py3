class Solution:
	def countSubTrees(self, n, edges, labels):
		arr = [0 for _ in range(n)]
		#build a graph with reverse edges
		#mark the leaf nodes in separate list
		lSet = set()
		dc = {}
		for src,dest in edges:
			dc[dest] = src
			lSet.add(dest)
			lSet.discard(src)
		#print("dc",dc)
		#print("lSet",lSet)

		def dfs(nd):
			d = {}
			st = [nd]
			while st:
				kx = st.pop()
				#print("curEl",kx)
				d[labels[kx]] = d.get(labels[kx],0) + 1
				#print(d[labels[kx]])
				arr[kx] = max(d[labels[kx]],arr[kx]+1)
				if(kx in dc):
					st.insert(0,dc[kx])
				#print("dict",d)
				#print("st",st)
		while lSet:
			dfs(lSet.pop())
		return arr
s=Solution()
n=4
e =[[0,1],[1,2],[0,3]]
st = "bbbb"
print(s.countSubTrees(n,e,st))
