'''
给你两个二进制字符串，返回它们的和（用二进制表示）。
输入为 非空 字符串且只包含数字1和0。

示例1:
输入: a = "11", b = "1"
输出: "100"

示例2:
输入: a = "1010", b = "1011"
输出: "10101"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-binary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a:
            return  b
        if not b:
            return a
        i,j=len(a)-1,len(b)-1
        sum=[]
        carry=0  # 进位
        while i>=0 or j>=0:
            if i>=0:
                carry+=int(a[i])
            if j>=0:
                carry+=int(b[j])
            i-=1
            j-=1
            sum.append(str(carry%2))
            carry>>=1
        sum.reverse()
        res=''.join(sum)
        return '1'+res if carry>0 else res




