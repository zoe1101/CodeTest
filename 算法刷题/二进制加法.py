'''
给定两个 01字符串a和b，请计算它们的和，并以二进制字符串的形式输出。
输入为 非空 字符串且只包含数字1和0。

示例:
输入: a = "11", b = "10"
输出: "101"

思路：将两个字符串进行右端对齐，然后从它们的个位开始从右往左相加同一位置的两个数位，若前一位有进位则还需加上进位。每位计算的结果push进结果ret，最后将结果进行翻转就行。

'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry=0
        n1=len(a)-1
        n2=len(b)-1
        res=''
        while n1>=0 or n2>=0:  ##从低位开始计算
            dig_a =int(a[n1]) if n1>=0 else 0
            n1 -= 1
            dig_b =int(b[n2]) if n2>=0 else 0
            n2 -= 1
            sum = (dig_a ^ dig_b) ^ carry
            carry = (dig_a & dig_b) | ((dig_a | dig_b) & carry)
            # sum =0 if dig_a+dig_b+carry==2 else 1
            # carry=1 if dig_a+dig_b+carry>1 else 0
            res+=str(sum)
        if carry:
            res+='1'
        return res[::-1]
if __name__ == '__main__':
    print(Solution().addBinary(a='1',b='111'))



