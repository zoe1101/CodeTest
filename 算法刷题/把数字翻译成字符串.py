'''
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
思路：动态递归
故状态转移函数为：
前面两个数在1–25之间，dp(i)=dp(i−2)+dp(i−1)。如果只翻译自己，比如 12345，如果 5独翻译，那么方法数与 1234 是一样的， dp(i)=dp(i-1)
else，dp(i)=dp(i−1)

再考虑边界条件：
dp(0)=dp(1)=1

'''

class Solution:
    def translateNum(self, num: int) -> int:
        str_num = str(num)
        n = len(str_num)
        dp = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            if str_num[i - 2] == '1' or (str_num[i - 2] == '2' and str_num[i - 1] < '6'):
                dp[i] = dp[i - 2] + dp[i - 1]
            else:
                dp[i] = dp[i - 1]
        return dp[n]

if __name__ == '__main__':
    while True:
        n = int(input('请输入n：'))
        print(Solution().translateNum(n))