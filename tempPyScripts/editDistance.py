class Solution(object):
    def minDistance(self, word1, word2):
        if(word1==word2==""):
            return(0)
        elif(word1=="" or word2==""):
            return(max(len(word1),len(word2)))
        arr=[[0]*len(word1) for _ in range(len(word2)) ]
        x=word2[0]
        cnX=0
        #print(tmpArr1)
        flagX,flagY=False,False
        for i in range(len(word1)):
            if(word1[i]==x and not flagX):
                flagX=True
                arr[0][i]=cnX
            else:
                cnX+=1
                arr[0][i]=cnX
        y=word1[0]
        #print(tmpArr1)
        #for i in arr:
        #    print(i)
        if(y==x):
            flagY=True
        cnY=arr[0][0]
        for i in range(1,len(word2)):
            if(word2[i]==y and not flagY):
                flagY=True
                arr[i][0]=cnY
            else:
                cnY+=1
                arr[i][0]=cnY
        #for i in arr:
        #    print(i)
        for j in range(1,len(word1)):
            for i in range(1,len(word2)):
                #print(i,j)
                #k=tmpArr1[i-1][j]
                #k1=tmpArr1[i-1][j-1]
                #k2=tmpArr1[i][j-1]
                if(word1[j]==word2[i]):
                    arr[i][j]=arr[i-1][j-1]
                else:
                    k=arr[i-1][j]
                    k1=arr[i-1][j-1]
                    k2=arr[i][j-1]
                    arr[i][j]=1+min(k1,k2,k)
        #print(arr)
        for i in arr:
            print(i)
        return(arr[-1][-1])
s=Solution()
s1,s2="sea","ate"
print(s.minDistance(s1,s2))
