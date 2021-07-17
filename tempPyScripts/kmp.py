class Solution:
    def strStr(self, text: str, pattern: str) -> int:
        arr=[0]*len(pattern)
        j=0
        for i in range(1,len(pattern)):
            if(pattern[i]==pattern[j]):
                j+=1
                arr[i]=j

            else:
                if(j!=0):
                    j=arr[j-1]
                else:
                    arr[i]=0
        #print(arr)

        i,j=0,0
        while(i<len(text) and j<len(pattern)):
            if(text[i]==text[j]):
                i+=1
                j+=1
                if(j==len(pattern)):
                    return(i-j)
            else:
                if(j!=0):
                    j=arr[j-1]
                else:
                    i+=1
        return(-1)
s=Solution()
print(s.strStr("hello","ll"))
