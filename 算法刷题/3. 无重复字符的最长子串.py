'''
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

思路：动态规划 + 哈希表 【滑动窗口】
设动态规划列表 dp，dp[j]代表以字符 s[j]为结尾的 “最长不重复子字符串” 的长度。

哈希表统计： 遍历字符串 s 时，使用哈希表（记为 dic）统计 各字符最后一次出现的索引位置 。
左边界 i获取方式： 遍历到 s[j] 时，可通过访问哈希表 dic[s[j]] 获取最近的相同字符的索引 i 。
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k, res, c_dict = -1, 0, {}
        for i, c in enumerate(s):
            if c in c_dict and c_dict[c] > k:  # 字符c在字典中 且 上次出现的下标大于当前长度的起始下标
                k = c_dict[c]
                c_dict[c] = i
            else:
                c_dict[c] = i
                res = max(res, i-k)
        return res

    def lengthOfLongestSubstring2(self, s: str) -> int:
        '''滑动窗口'''
        if not s or len(s)==0:
            return 0
        res,l=0,0  ##l 表示第一个不重复字符的位置
        for i in range(len(s)):
            for j in range(l,i):
                if s[j]==s[i]:
                    l=j+1
                    break
            res=max(res,i-l+1)
        return res

if __name__ == '__main__':
    while True:
        s=input('请输入字符串：')
        print(Solution().lengthOfLongestSubstring2(s))