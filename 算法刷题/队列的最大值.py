'''
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
若队列为空，pop_front 和 max_value需要返回 -1

输入:
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出:[null,null,null,2,1,2]

'''
import collections
import queue


class MaxQueue:

    def __init__(self):
        self.queue = [] ##正常的队列，负责push和pop
        self.maxq = [] ##存储包含当前队列元素的单调递减队列，队首就是最大值。来存放最大值

    def max_value(self) -> int:
        return self.maxq[0] if self.maxq else -1


    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.maxq and self.maxq[-1]<value:
            self.maxq.pop()
        self.maxq.append(value)

    def pop_front(self) -> int:
        if not self.maxq:
            return -1
        v=self.queue.pop(0)
        if v==self.maxq[0]:
            self.maxq.pop(0)
        return v



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()