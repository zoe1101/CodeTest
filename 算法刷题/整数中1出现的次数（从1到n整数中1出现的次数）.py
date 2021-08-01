'''
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。

思路:将 1 ~ n 的个位、十位、百位、...的 1 出现次数相加，即为 1出现的总次数。
参考：https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/solution/mian-shi-ti-43-1n-zheng-shu-zhong-1-chu-xian-de-2/
设数字N是一个x位数，记N的第i位为Ni，则可将N表示为NxNx-1...N2N1
称Ni为当前位，记为cur
Ni-1...N2N1称为低位，记为low
NNxNx-1...Ni+1称为高位，记为high
将10^i称为位因子，记为digit
计算当前位Ni中 1出现次数，根据当前位 cur值的不同，分为以下三种情况：
cur=0：high×digit，此位 1的出现次数只由高位 high决定
cur=1：high×digit+low+1，此位 1 的出现次数由高位 high和低位 low 决定
2<=cur<=9：(high+1)×digit，此位 1的出现次数只由高位 high决定

'''
class Solution:
    def countDigitOne(self, n: int) -> int:
        #从右至左
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            if cur == 0: res += high * digit
            elif cur == 1: res += high * digit + low + 1
            else: res += (high + 1) * digit
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        return res

if __name__ == '__main__':
    while True:
        n = int(input('请输入n：'))
        print(Solution().countDigitOne(n))
