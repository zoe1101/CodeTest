'''
给定一种规律 pattern和一个字符串str，判断 str 是否遵循相同的规律。
这里的遵循指完全匹配，例如，pattern里的每个字母和字符串str中的每个非空单词之间存在着双向连接的对应规律。

输入: pattern = "abba", str = "dog cat cat dog"
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_list=list(pattern)
        s_list=s.split()
        return len(p_list)==len(s_list) and len(set(p_list))==len(set(s_list))==len(set(zip(p_list,s_list)))