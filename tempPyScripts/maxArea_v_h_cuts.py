class Solution:
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        res=[(0,h,0,w)]
        #print(res)
        mx=0
        for i in horizontalCuts:
            #print(i)
            r=[]
            while(res):
                #k=res.pop()
                x1,x2,y1,y2=res.pop()
                if(x2>i>x1):
                    k=(x1,i,y1,y2)
                    r.append(k)
                    #print(k)
                    k=(i,x2,y1,y2)
                    r.append(k)
                    #print(k)
                    #mx=max(mx,(i-x1)*(y2-y1),(x2-i)*(y2-y1))
                else:
                    k=(x1,x2,y1,y2)
                    r.append(k)
                    #print(k)
            r,res=res,r
        for i in verticalCuts:
            #print(i)
            r=[]
            while(res):
                x1,x2,y1,y2=res.pop()
                if(y2>i>y1):
                    k=(x1,x2,y1,i)
                    r.append(k)
                    #print(k)
                    k=(x1,x2,i,y2)
                    r.append(k)
                    #print(k)
                    #mx=max(mx,(i-x1)*(y2-y1),(x2-i)*(y2-y1))
                else:
                    k=(x1,x2,y1,y2)
                    r.append(k)
                    #print(k)
                    #mx=max(mx,(x2-x1)*(y2-y1))
            r,res=res,r
        #print(res)
        for i in range(len(res)):
            x1,x2,y1,y2=res[i]
            mx=max(mx,(x2-x1)*(y2-y1))
        return(mx)
s=Solution()
h=5
w=4
hc=[1,2,4]
vc=[1,3]
print(s.maxArea(h,w,hc,vc))
