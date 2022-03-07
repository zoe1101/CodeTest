'''
有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你 不能 重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。

示例 1：

输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/restore-ip-addresses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
from typing import List



class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []  # 存放分割后的字符

        # 判断数组中的数字是否合法
        def isValid(p):
            if p == '0': return True  # 解决"0000"
            if p[0] == '0': return False
            if int(p) > 0 and int(p) < 256: return True
            return False

        def backtrack(s, startIndex):
            if len(s) > 12: return  # 字符串长度最大为12
            if len(path) == 4 and startIndex == len(s):  # 确保切割完，且切割后的长度为4
                res.append(".".join(path[:]))  # 字符拼接
                return

            for i in range(startIndex, len(s)):
                if len(s) - startIndex > 3 * (4 - len(path)): continue  # 剪枝，剩下的字符串大于允许的最大长度则跳过
                p = s[startIndex:i + 1]  # 分割字符
                if isValid(p):  # 判断字符是否有效
                    path.append(p)
                else:
                    continue
                backtrack(s, i + 1)  # 寻找i+1为起始位置的子串
                path.pop()

        backtrack(s, 0)
        return res


if __name__ == '__main__':
    s='010010'
    print(Solution().restoreIpAddresses(s))


