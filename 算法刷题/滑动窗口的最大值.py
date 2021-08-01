'''
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]

思路：双端单调队列

遍历数组时，每轮保证单调队列 dequedeque ：

deque 内 仅包含窗口内的元素 ⇒ 每轮窗口滑动移除了元素nums[i−1] ，需将 deque 内的对应元素一起删除。
deque内的元素 非严格递减⇒ 每轮窗口滑动添加了元素nums[j+1] ，需将 deque内所有<nums[j+1] 的元素删除。

算法流程：
初始化： 双端队列 dequedeque ，结果列表 resres ，数组长度 nn ；
滑动窗口： 左边界范围 i∈[1−k,n−k] ，右边界范围 j∈[0,n−1] ；
若i>0 且 队首元素 deque[0]==被删除元素 nums[i−1] ：则队首元素出队；
删除 deque 内所有 <nums[j] 的元素，以保持 deque递减；
将 nums[j] 添加至 deque 尾部；
若已形成窗口（即 i≥0 ）：将窗口最大值（即队首元素 deque[0]）添加至列表 res；
返回值： 返回结果列表 res ；

'''
import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or len(nums)<k:
            return []
        deque=collections.deque()
        # 未形成窗口
        for i in range(k):
            while deque and deque[-1]<nums[i]:
                deque.pop()
            deque.append(nums[i])
        res = [deque[0]]
        # 形成窗口后
        for i in range(k,len(nums)):
            if deque[0] == nums[i - k]:  ##队首元素等于待删除的左窗口元素
                deque.popleft()
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res
