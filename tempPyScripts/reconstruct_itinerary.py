from collections import defaultdict
from sortedcontainers import SortedList
class Solution:
    def findItinerary(self, tickets):
        d = defaultdict(SortedList)
        for src,dest in tickets:
            #d[src].append(dest)
            d[src].add(dest)
        res = []
        print(d)
        '''
        st=["JFK"]
        while(st):
            k=st.pop(0)
            res.append(k)
            if(len(d[k])>0):
                l = d[k].pop(0)
                st.append(l)
        return(res)
        '''
        src = "JFK"
        res.append(src)
        while(True):
            if(len(d[src])==0):
                #return(res)
                break
            #res.append(src)
            src = d[src].pop(0)
            res.append(src)
        return(res)
s=Solution()
arr = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
print(s.findItinerary(arr))
