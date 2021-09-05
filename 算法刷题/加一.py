'''
定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。


输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

'''
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1],carry = (digits[-1] + 1) % 10,(digits[-1]+1)//10
        for i in range(len(digits)-2,-1,-1):
            digits[i],carry= (carry + digits[i]) % 10,(carry+digits[i])//10

        if carry>0:
            digits.insert(0,carry)
        return digits

if __name__ == '__main__':
    digits=[1,2,4]
    print(Solution().plusOne(digits))

