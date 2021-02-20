'''
要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0），n<=39。
斐波那契数列:F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）
'''

class Solution:
    def Fibonacci(self, n):
        if n<1:
            return 0
        f=[0,1,1]
        for i in range(3,n+1):
            f.append(f[i-2]+f[i-1])
        return f[n]

if __name__ == '__main__':
    while True:
        n=input('请输入n：')
        print(Solution().Fibonacci(int(n)))