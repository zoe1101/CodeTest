'''
给你一个字符串columnTitle ，表示 Excel 表格中的列名称。返回该列名称对应的列序号。

例如，
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

示例 1:
输入: columnTitle = "A"
输出: 1


示例2:
输入: columnTitle = "AB"
输出: 28

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/excel-sheet-column-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res=0
        for i in range(len(columnTitle)):
            res=res*26+(ord(columnTitle[i])-ord('A')+1)
        return res

