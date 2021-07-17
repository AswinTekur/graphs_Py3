class Solution:
    def merge(self, intervals):
        if(len(intervals)<2):
            return(intervals)
        def merge(st,en,st1,en1):
            if(st==en==None):
                return([1,st1,en1])
            else:
                if(st1<en):
                    return([1,st,en1])
                return([2,st,en,st1,en1])
        i,j=0,0
        st,en=None,None
        res=[]
        while(intervals):
            k=intervals.pop(0)
            sx=merge(st,en,k[0],k[1])
            #print(sx)
            if(sx[0]==1):
                st,en=sx[1],sx[2]
            else:
                res.append([sx[1],sx[2]])
                st,en=sx[3],sx[4]
        res.append([st,en])
        return(res)
arr=[[1,3],[2,6],[8,10],[15,18]]
s=Solution()
print(s.merge(arr))
