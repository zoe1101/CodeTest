class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):
    """二叉树"""
    def __init__(self):
        self._root = None

    def max_depth(self,node):
        '''最大深度'''
        return 1+max(self.max_depth(node.left),self.max_depth(node.right)) if node else 0

    def add(self, item):
        node=TreeNode(item)
        if self._root is None:
            self._root=node
            return
        tmp_queue=[self._root]
        while True:
            curnode=tmp_queue.pop(0)
            if curnode is None:
                return
            if curnode.left is None:
                curnode.left=node
                return
            if curnode.right is None:
                curnode.right=node
                return
            tmp_queue.append(curnode.left)
            tmp_queue.append(curnode.right)

    def front_travel(self, node):
        """先序遍历"""
        if node is None:
            return
        print(node.val,end=" ")
        self.front_travel(node.left)
        self.front_travel(node.right)

    def middle_travel(self, node):
        """中序遍历"""
        if node is None:
            return
        self.middle_travel(node.left)
        print(node.val,end=" ")
        self.middle_travel(node.right)


    def last_travel(self, node):
        """后序遍历"""
        if node is None:
            return
        self.last_travel(node.left)
        self.last_travel(node.right)
        print(node.val,end=" ")

    def level_travel(self):
        """层次遍历"""
        tmp_queue=[self._root]
        while True:
            if len(tmp_queue)==0:##遍历完成
                return
            curnode=tmp_queue.pop(0)
            print(curnode.val,end=" ")
            if curnode.left:
                tmp_queue.append(curnode.left)
            if curnode.right:
                tmp_queue.append(curnode.right)

if __name__ == '__main__':
    tree=Tree()
    for i in range(9):
        tree.add(i)
    tree.front_travel(tree._root)  # 递归前序遍历
    print()
    tree.middle_travel(tree._root)  # 递归中序遍历
    print()
    tree.last_travel(tree._root)  # 递归后序遍历
    print()
    tree.level_travel()  ## 层次遍历
    print()
