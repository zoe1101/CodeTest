'''
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

例如，121 是回文，而 123 不是。
 

示例 1：

输入：x = 121
输出：true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):#如果是负数或者这个数个位为0，则返回false（0除外）
            return False
        # 反转一半数字，例如，输入 1221，我们可以将数字 “1221” 的后半部分从 “21” 反转为 “12”，并将其与前半部分 “12” 进行比较，因为二者相同，我们得知数字 1221 是回文。

        revertedNumber=0  #记录逆转的一半
        while x>revertedNumber:
            revertedNumber=revertedNumber*10+x%10  ##
            x//=10
        return x==revertedNumber or x==revertedNumber//10 #rev==x:偶位数，x==rev/10：奇位数