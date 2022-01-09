'''
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例：

输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/array-and-string/c8su7/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

'''
class Solution:
    def reverseWords(self, s: str) -> str:
        s=list(s)
        s.reverse()
        n=len(s)
        left=0
        right=n-1
        while left<n and s[left]==" ":
            left+=1

        while right<n and s[right]==" ":
            right-=1
        res=[]
        while left<=right:
            index = right
            while index>=left and s[index]!=' ':
                index-=1
            for i in range(index+1,right+1):
                res.append(s[i])
            if index>left:
                res.append(' ')
            while index>=left and s[index]==' ':
                index-=1

            right=index
        return ''.join(res)
if __name__ == '__main__':
    s=r"Let's take LeetCode contest"
    print(Solution().reverseWords(s))
