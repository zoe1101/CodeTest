class ListNode:
    """单链表的结点"""
    def __init__(self, x):
        self.item = x  #数据元素
        self.next = None  #下一个节点的标识

class Node(object):
    """双向链表的结点"""
    def __init__(self, item):
        # item存放数据元素
        self.item = item
        # next 指向下一个节点的标识
        self.next = None
        # prev 指向上一结点
        self.pre = None

## 单向链表
class SingleLinkList(object):
    """单链表"""
    def __init__(self):
        self._head=None
    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        curnode=self._head
        count=0
        while curnode is not None:
            count+=1
            curnode=curnode.next
        return count

    def items(self):
        """遍历链表，获取链表数据迭代器"""
        curnode=self._head
        while curnode is not None:
            yield curnode.item  # 返回生成器
            curnode=curnode.next

    def add(self,item):
        """向链表头部添加元素"""
        node=ListNode(item)
        node.next=self._head # 新结点指针指向原头部结点
        self._head=node # 头部结点指针修改为新结点

    def append(self,item):
        """尾部添加元素"""
        node=ListNode(item)
        # 先判断是否为空链表
        if self.is_empty(): # 空链表，_head 指向新结点
            self._head=node
        else:# 不是空链表，则找到尾部，将尾部next结点指向新结点
            curnode=self._head
            while curnode.next is not None:
                curnode=curnode.next
            curnode.next=node

    def insert(self,index,item):
        """指定位置插入元素"""
        # 指定位置在第一个元素之前，在头部插入
        if index<=0:
            self.add(item)
        elif index>=self.length():
            self.append(item)
        else:
            node=ListNode(item)
            curnode = self._head
            for i in range(index-1):
                curnode=curnode.next
            node.next=curnode.next
            curnode.next=node
    def remove(self,item):
        """删除节点"""
        curnode = self._head
        prenode=None
        while curnode is not None:
            if curnode.item==item:
                if not prenode:  #如果删除的的是第一个节点
                    self._head=curnode.next # 将头指针指向头节点的后一个节点
                else:# 将删除位置前一个节点的next指向删除位置的后一个节点
                    prenode.next=curnode.next
                return True
            else: # 继续按链表后移节点
                prenode=curnode
                curnode=curnode.next
    def find(self, item):
        """查找元素是否存在"""
        return item in self.items()

# 单向循环链表
class SingleCycleLinkList(object):
    def __init__(self):
        self._head=None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        # 链表为空
        if self.is_empty():
            return 0
        # 链表不为空
        count = 1
        curnode=self._head
        while curnode.next!=self._head:
            count+=1
            curnode=curnode.next # 指针下移
        return count
    def items(self):
        # 链表为空
        if self.is_empty():
            return
        # 链表不为空
        curnode = self._head
        while curnode.next != self._head:
            yield curnode.item
            curnode=curnode.next
        yield curnode.item  #返回最后一个节点数据元素

    def add(self, item):
        """ 头部添加结点"""
        node=ListNode(item)
        # 链表为空
        if self.is_empty():
            self._head=node
            node.next=self._head
        else:
            node.next=self._head # 添加结点指向head
            curnode=self._head
            while curnode.next!=self._head:
                curnode=curnode.next
            curnode.next=node
        self._head=node # 修改 head 指向新结点

    def append(self, item):
        """尾部添加结点"""
        node = ListNode(item)
        if self.is_empty():  # 链表为空
            self._head = node
            node.next = self._head
        else:
            curnode=self._head
            while curnode.next!=self._head: # 寻找尾部
                curnode=curnode.next
            curnode.next=node # 尾部指针指向新结点
            node.next=self._head # 新结点指针指向head

    def insert(self, index, item):
        """ 指定位置添加结点"""
        if index<=0: # 指定位置小于等于0，头部添加
            self.add(item)
        elif index>=self.length(): # 指定位置大于链表长度，尾部添加
            self.add(item)
        else: # 移动到添加结点位置
            node=ListNode(item)
            curnode=self._head
            for i in range(index-1):
                curnode=curnode.next
            node.next=curnode.next # 新结点指针指向旧结点
            curnode.next = node  # 旧结点指针 指向 新结点

    def remove(self, item):
        """ 删除一个结点 """
        if self.is_empty():
            return
        curnode=self._head
        prenode=ListNode
        if curnode.item == item: # 第一个元素为需要删除的元素
            if curnode.next!=self._head:# 链表不止一个元素
                while curnode.next!=self._head:
                    curnode=curnode.next
                curnode.next=self._head.next # 尾结点指向 头部结点的下一结点
                self._head=self._head.next # 调整头部结点
            else: # 只有一个元素
                self._head=None
        else: # 要删除的不是第一个元素
            pre = self._head
            while curnode.next!=self._head:
                if curnode.item==item:
                    prenode.next=curnode.next
                    return True
                else:
                    prenode=curnode # 记录前一个指针
                    curnode=curnode.next # 调整指针位置
            # 当删除元素在末尾
        if curnode.item == item:
            pre.next = self._head
            return True

    def find(self, item):
        """ 查找元素是否存在"""
        return item in self.items()


# 双向链表
class BilateralLinkList(object):
    """双向链表"""
    def __init__(self):
        self._head=None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        curnode=self._head
        count=0
        while curnode is not None:
            count+=1
            curnode=curnode.next

        return count

    def items(self):
        """遍历链表"""
        curnode=self._head
        while curnode is not None:
            yield curnode.item # 返回生成器
            curnode=curnode.next

    def add(self,item):
        """向链表头部添加元素"""
        node=Node(item)
        if self.is_empty():
            self._head=node # 头部结点指针修改为新结点
        else:
            node.next=self._head # 新结点指针指向原头部结点
            self._head.pre=node # 原头部 prev 指向 新结点
            self._head=node # head 指向新结点

    def append(self, item):
        """尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self._head=node # 头部结点指针修改为新结点
        else:
            curnode=self._head
            while curnode.next is not None:
                curnode=curnode.next
            node.pre=curnode # 新结点上一级指针指向旧尾部
            curnode.next=node # 旧尾部指向新结点

    def insert(self, index, item):
        """ 指定位置插入元素"""
        if index<=0:
            self.add(item)
        elif index>=self.length():
            self.append(item)
        else:
            curnode=self._head
            node=Node(item)
            for i in range(index-1):
                curnode=curnode.next
            node.next=curnode # 新结点的向下指针指向当前结点
            node.pre=curnode.pre  # 新结点的向上指针指向当前结点的上一结点
            curnode.pre.next=node # 当前上一结点的向下指针指向node
            curnode.pre=node  # 当前结点的向上指针指向新结点

    def remove(self, item):
        """ 删除结点 """
        if self.is_empty():
            return
        curnode=self._head
        if curnode.item==item: # 删除元素在第一个结点
            if curnode.next is None:  # 只有一个元素
                self._head=None
                return True
            else:
                self._head=curnode.next # head 指向下一结点
                curnode.next.pre=None # 下一结点的向上指针指向None
                return True
        # 移动指针查找元素
        while curnode.next is not None:
            if curnode.item==item:
                curnode.pre.next=curnode.next # 上一结点向下指针指向下一结点
                curnode.next.pre=curnode.pre # 下一结点向上指针指向上一结点
                return True
            curnode=curnode.next
        # 删除元素在最后一个
        if curnode.item==item:
            curnode.pre.next=None # 上一结点向下指针指向None
            return True

    def find(self, item):
        """查找元素是否存在"""
        return item in self.items()


# 双向循环链表
class BilateralCycleLinkList(object):
    """双向链表"""
    def __init__(self):
        self._head=None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        count=1
        curnode = self._head
        while curnode.next != self._head:
            count+=1
            curnode=curnode.next
        return count

    def items(self):
        """遍历链表"""
        if self.is_empty():
            return None
        curnode=self._head
        while curnode.next!=self._head:
            yield curnode.item # 返回生成器
            curnode=curnode.next
        yield curnode.item

    def add(self,item):
        """向链表头部添加元素"""
        node=Node(item)
        if self.is_empty():
            node.next=node
            node.pre=node
            self._head=node # 头部结点指针修改为新结点
        else:
            curnode = self._head
            node.next=curnode # 新结点指针指向原头部结点
            node.pre=curnode
            if curnode.next == self._head:  #只有一个节点的情况
                curnode.pre=node
                curnode.next=node
                self._head=node
            else:
                headnode = self._head
                while curnode.next!=self._head:
                    curnode=curnode.next
                headnode.pre=node
                curnode.next = node
                self._head=node

    def append(self, item):
        """尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            node.next=node
            node.pre=node
            self._head=node # 头部结点指针修改为新结点
        else:
            curnode = self._head
            self._head.pre=node  # 指针指向最后一个节点
            node.next=self._head
            while curnode.next!=self._head:
                curnode=curnode.next
            curnode.next=node
            node.pre=curnode

    def insert(self, index, item):
        """ 指定位置插入元素"""
        if index<=0:
            self.add(item)
        elif index>=self.length():
            self.append(item)
        else:
            curnode=self._head
            node=Node(item)
            for i in range(index-1):
                curnode=curnode.next
            node.next=curnode # 新结点的向下指针指向当前结点
            node.pre=curnode.pre  # 新结点的向上指针指向当前结点的上一结点
            curnode.pre.next=node # 当前上一结点的向下指针指向node
            curnode.pre=node  # 当前结点的向上指针指向新结点

    def remove(self, item):
        """ 删除结点 """
        if self.is_empty():
            return
        curnode=self._head
        if curnode.item==item: #如果删除的是头节点
            if curnode.next !=self._head:  # 只有一个元素
                self._head=None
                return True
            else:
                headnode=curnode.next # head 指向下一结点
                while curnode.next!=self._head:
                    curnode=curnode.next
                curnode.next=headnode.next
                headnode.pre=curnode.next
                self._head=headnode.next
                return True
        # 移动指针查找元素
        while curnode.next!=self._head:
            if curnode.item==item:
                curnode.pre.next=curnode.next # 上一结点向下指针指向下一结点
                curnode.next.pre=curnode.pre # 下一结点向上指针指向上一结点
                return True
            curnode=curnode.next
        # 删除元素在最后一个
        if curnode.item==item:
            curnode.pre.next=self._head
            self._head.pre = curnode.pre
            return True

    def find(self, item):
        """查找元素是否存在"""
        return item in self.items()




if __name__ == '__main__':
    # linklist=SingleLinkList()
    # node1=ListNode(1)
    # node2=ListNode(2)
    # linklist._head=node1
    # node1.next=node2
    # print(linklist._head.item)  # 访问第一个结点数据
    # print(linklist._head.next.item)  # 访问第二个结点数据

 ## 单向链表
    # link_list = SingleLinkList()
    # # 向链表尾部添加数据
    # for i in range(5):
    #     link_list.append(i)
    # # 向头部添加数据
    # link_list.add(6)
    # # 遍历链表数据
    # for i in link_list.items():
    #     print(i, end='\t')
    # # 链表数据插入数据
    # link_list.insert(3, 9)
    # print('\n', list(link_list.items()))
    # # 删除链表数据
    # link_list.remove(0)
    # # 查找链表数据
    # print(link_list.find(4))


  # 单向循环链表
    # link_list = SingleCycleLinkList()
    # print(link_list.is_empty())
    # # 头部添加元素
    # for i in range(5):
    #     link_list.add(i)
    # print(list(link_list.items()))
    # # 尾部添加元素
    # for i in range(6):
    #     link_list.append(i)
    # print(list(link_list.items()))
    # # 添加元素
    # link_list.insert(3, 45)
    # print(list(link_list.items()))
    # # 删除元素
    # link_list.remove(5)
    # print(list(link_list.items()))
    # # 元素是否存在
    # print(4 in link_list.items())

  #双向链表
    # link_list = BilateralLinkList()
    # print(link_list.is_empty())
    # # 头部添加元素
    # for i in range(5):
    #   link_list.add(i)
    # print(list(link_list.items()))
    # # 尾部添加元素
    # for i in range(6):
    #   link_list.append(i)
    # print(list(link_list.items()))
    # # 添加元素
    # link_list.insert(3, 45)
    # print(list(link_list.items()))
    # # 删除元素
    # link_list.remove(5)
    # print(list(link_list.items()))
    # # 元素是否存在
    # print(4 in link_list.items())

  ##双向循环链表
    link_list = BilateralCycleLinkList()
    print(link_list.is_empty())
    # 头部添加元素
    for i in range(5):
        link_list.add(i)
    print(list(link_list.items()))
    # 尾部添加元素
    for i in range(6):
        link_list.append(i)
    print(list(link_list.items()))
    # 添加元素
    link_list.insert(3, 45)
    print(list(link_list.items()))
    # 删除元素
    link_list.remove(1)
    print(list(link_list.items()))
    # 元素是否存在
    print(4 in link_list.items())