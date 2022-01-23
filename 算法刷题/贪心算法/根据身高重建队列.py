'''
假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不一定按顺序）。每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，前面 正好 有 ki 个身高大于或等于 hi 的人。

请你重新构造并返回输入数组people 所表示的队列。返回的队列应该格式化为数组 queue ，其中 queue[j] = [hj, kj] 是队列中第 j 个人的属性（queue[0] 是排在队列前面的人）。


示例 1：

输入：people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
输出：[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
解释：
编号为 0 的人身高为 5 ，没有身高更高或者相同的人排在他前面。
编号为 1 的人身高为 7 ，没有身高更高或者相同的人排在他前面。
编号为 2 的人身高为 5 ，有 2 个身高更高或者相同的人排在他前面，即编号为 0 和 1 的人。
编号为 3 的人身高为 6 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
编号为 4 的人身高为 4 ，有 4 个身高更高或者相同的人排在他前面，即编号为 0、1、2、3 的人。
编号为 5 的人身高为 7 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
因此 [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] 是重新构造后的队列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/queue-reconstruction-by-height
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 从高到低考虑
        n = len(people)
        if n<2:
            return people
        res=[]
        people.sort(key=lambda x:(-x[0],x[1]))  #按照 h_i为第一关键字降序，k_i为第二关键字升序进行排序
        for p in people:
            res[p[1]:p[1]]=[p] # 等同于在p[1]位置插入元素p， ==  res.insert(p[1],p)
        return res

    def reconstructQueue1(self, people: List[List[int]]) -> List[List[int]]:
        # 从低到高考虑
        n = len(people)
        if n < 2:
            return people
        res = [[]*n]
        people.sort(key=lambda x: (x[0], -x[1]))  # 按照 h_i为第一关键字升序，k_i为第二关键字降序进行排序
        for p in people:
            space=p[1]+1
            for i in range(n):
                if not res[i]:
                    space-=1
                    if space==0:
                        res[i]=p
                        break
        return res


