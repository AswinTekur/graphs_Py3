class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if(len(s)<2):
            return(len(s))
        n=len(s)
        dp=[1]*n
        for j in range(1,n):
            pre=dp[j]
            for i in range(j-1,-1,-1):
                tmp=dp[i]
                if(s[i]==s[j]):
                    dp[i]= 2 + pre if j>=i+2 else 2
                else:
                    dp[i]=max(dp[i],dp[i+1])
                pre=tmp
        return(dp[0])
s=Solution()
s1="abac"
print(s.longestPalindromeSubseq(s1))
