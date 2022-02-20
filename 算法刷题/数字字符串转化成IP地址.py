'''
现在有一个只包含数字的字符串，将该字符串转化成IP地址的形式，返回所有可能的情况。
例如：
给出的字符串为"25525522135",
返回["255.255.22.135", "255.255.221.35"]. (顺序没有关系)

数据范围：字符串长度 0 \le n \le 120≤n≤12
要求：空间复杂度 O(n!)O(n!),时间复杂度 O(n!)O(n!)

注意：ip地址是由四段数字组成的数字序列，格式如 "x.x.x.x"，其中 x 的范围应当是 [0,255]。

示例1
输入：
"25525522135"
复制
返回值：
["255.255.22.135","255.255.221.35"]

'''
from typing import List





class Solution:
    def restoreIpAddresses(self , s: str) -> List[str]:
        '''递归回溯,深度优先搜索DFS
        ip地址限制条件：
            ip地址一共包含4段，每段用 '.'分隔
            每段如果有两位及以上，则首位不能为0，如01，02
            每段不能大于255
        '''


        def dfs(s, res, temp):
            if len(s)==0 and len(temp)==4:
                res.append('.'.join(temp))
            for n in range(1,len(s)+1): # 这里的n不是索引，是子字符串的长
                if s[0]=='0' and n>1: # 如果有两位及以上每段的首位不能为0
                    return
                val=s[0:n]
                if int(val)>255: # ip地址每段不能大于255
                    return
                temp.append(val)  #符合条件插入候选数组
                dfs(s[n:],res,temp) # 递归搜素下一段
                temp.remove(val) #清除temp，确保下一组ip不受影响

        if len(s)<4 or len(s)>12:
            return []
        res=[]
        temp=[]
        dfs(s,res,temp)
        return res

if __name__ == '__main__':
    s='010010'
    print(Solution().restoreIpAddresses(s))


