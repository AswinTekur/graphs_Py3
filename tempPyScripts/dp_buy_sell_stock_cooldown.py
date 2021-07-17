class Solution:
    def maxProfit(self, prices):
        if(len(prices)==0):
            return(0)
        '''
        l=len(prices)
        mp=[0]*(2+l)
        for i in range(l-2,-1,-1):
            c2=mp[i+1]
            c1=0
            for sell in range(i+1,l):
                c1=max(c1,prices[sell]-prices[i]+mp[sell+2])
            mp[i]=max(c1,c2)
        return(mp[0])
        '''
        #b,s,r=[0]*len(prices),[0]*len(prices),[0]*len(prices)
        b,s,r=[0]*2,[0]*2,[0]*2
        b[0]=-prices[0]
        for i in range(1,len(prices)):
            #print(indx)
            indx=(i-1)%2
            print(indx)
            b[i]=max(b[indx],r[indx]-prices[i])
            r[i]=max(r[indx],s[indx])
            s[i]=b[indx]+prices[i]
        return(max(r[-1],s[-1]))
s=Solution()
arr=[1,2,3,0,2]
print(s.maxProfit(arr))
