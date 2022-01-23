'''
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：

对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。


示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
示例 2：

输入：s = "a", t = "a"
输出："a"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        needCnt = len(t)
        minLeft, minRight = 0, len(s)
        for c in t:
            need[c] += 1
        left=0
        for right,c in enumerate(s):
            if need[c]>0:
                needCnt-=1
            need[c]-=1
            if needCnt==0:  #步骤一：不断增加right使滑动窗口增大，直到窗口包含了T的所有元素
                while need[s[left]]<0:  #步骤二：不断增加left使滑动窗口缩小，因为是要求最小字串，所以将不必要的元素排除在外，使长度减小，直到碰到一个必须包含的元素，这个时候不能再扔了，再扔就不满足条件了，记录此时滑动窗口的长度，并保存最小值
                    need[s[left]]+=1
                    left+=1
                if right-left<minRight-minLeft: #记录结果
                    minLeft,minRight = left,right
                need[s[left]]+=1 #步骤三：让left再增加一个位置，这个时候滑动窗口肯定不满足条件了，那么继续从步骤一开始执行，寻找新的满足条件的滑动窗口，如此反复，直到right超出了字符串S范围。
                needCnt+=1
                left+=1
        return '' if minRight==len(s) else s[minLeft:minRight+1]   #如果res始终没被更新过，代表无满足条件的结果
