def editDistance(s1,s2):
    m,n=len(s1),len(s2)
    if m==0 or n==0:
        return max(m,n)
    dp=[[0]*(n+1) for _ in range(m+1)] #dp[i][j] 代表着word1的前i个字符转换成word2的前j个字符所需要的最少操作步数
    dp[0][0]=0
    for i in range(m):
        dp[i][0]=i
    for j in range(n):
        dp[0][j]=j
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
    return dp[m][n]

if __name__ == '__main__':
    s1='4'
    s2='1234'
    print(editDistance(s1,s2))