'''
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。

 

示例：

输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-labels
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last=[0]*26
        for i,c in enumerate(s):
            last[ord(c)-ord('a')]=i
        res=[]
        start,end=0,0
        for i,c in enumerate(s):
            end=max(end,last[ord(c)-ord('a')])
            if i==end:
                res.append(end-start+1)
                start=i+1
        return res