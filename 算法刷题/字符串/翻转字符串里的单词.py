'''
给你一个字符串 s ，逐个翻转字符串中的所有 单词 。
单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
请你返回一个翻转 s 中单词顺序并用单个空格相连的字符串。

说明：
输入字符串 s 可以在前面、后面或者单词间包含多余的空格。
翻转后单词间应当仅用一个空格分隔。
翻转后的字符串中不应包含额外的空格。


示例 1：

输入：s = "the sky is blue"
输出："blue is sky the"

思路：双指针法
题解参考：https://leetcode-cn.com/problems/reverse-words-in-a-string/solution/yi-ci-bian-li-shi-xian-fan-zhuan-zi-fu-c-cmos/
关键点：
如何修剪掉两端空格；
如何把单词反转过来；
如何跳过中间连续的空格。

'''
class Solution:
    def reverseWords(self, s: str) -> str:
        left=0
        right=len(s)-1
        res=[]
        # 修剪掉两端空格
        while s[left]==' ':
            left+=1
        while s[right]==' ':
            right-=1

        while left<=right:
            idx=right
            while(idx>=left and s[idx]!=' '):
                idx-=1
            # 把单词反转过来
            for i in range(idx+1,right+1):
                res.append(s[i])
            if idx>left:
                res.append(' ')
            # 跳过中间连续的空格
            while idx>=left and s[idx]==' ':
                idx-=1
            right=idx
        return ''.join(res)



