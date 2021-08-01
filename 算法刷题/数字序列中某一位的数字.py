'''
数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。
请写一个函数，求任意第n位对应的数字。

思路：
根据以上分析，可将求解分为三步：

确定 n所在数字的位数 ，记为 digit；循环执行 n减去 一位数、两位数、... 的数位数量 count，直至n≤count 时跳出。由于 n已经减去了一位数、两位数、...、(digit−1) 位数的 数位数量 count ，因而此时的 nn 是从起始数字 start开始计数的。
确定 n所在的 数字 ，记为 num；所求数位 在从数字 start开始的第 [(n−1)/digit] 个 数字 中（ start为第 0 个数字）。
确定 n是 num中的哪一数位，并返回结果。所求数位为数字 num 的第 (n-1)%digit位（ 数字的首个数位为第 0 位）

'''

class Solution:
    def findNthDigit(self, n):
        digit, start, count = 1, 1, 9
        while n > count: # 1.
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n - 1) // digit # 2.
        return int(str(num)[(n - 1) % digit]) # 3.

if __name__ == '__main__':
    while True:
        n = int(input('请输入n：'))
        print(Solution().findNthDigit(n))


