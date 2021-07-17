class Solution:
    def isPathCrossing(self, path: str) -> bool:
        ky = (0,0)
        s = set()
        s.add(ky)
        st = [0,0]
        for i in path:
            #if(tuple(st) in s):
            #    return(True)
            if(i=='N'):
                st[1]+=1
                #s.add(tuple(s))
            elif(i=='S'):
                st[1] -=1
            elif(i=='W'):
                st[0]-=1
            else:
                st[0]+=1
            print(i,st,s)
            kx = tuple(st)
            if(kx in s):
                return(True)
            s.add(kx)
        return(False)
s = Solution()
print("solution",s.isPathCrossing("NESWW"))
