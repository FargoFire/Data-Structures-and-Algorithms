# -*- coding: utf-8 -*-
"""
    Date: 2018/11/26
    By:  Fargo
    二叉树，二叉树遍历
    root 根节点，lchild 左子节点， rchlid 右子节点， elem 节点
"""

class Node(object):
    """节点类"""
    def __init__(self, elem = -1):
        self.elem = elem
        self.lchild = None
        self.rchild = None

class Tree(object):
    """树类"""
    def __init__(self):
        self.root = Node()
        self.my_queue = []

    def add_elem(self, elem):
        """增加节点"""
        node = Node(elem)
        # print('my_queue:  ',self.my_queue)
        if self.root.elem == -1:     # 树为空，根节点赋值
            self.root = node
            self.my_queue.append(self.root)

        else:
            treeNode = self.my_queue[0]   # 此结点的子树还没有齐。
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.my_queue.append(treeNode.lchild)

            else:
                treeNode.rchild = node
                self.my_queue.append(treeNode.rchild)
                self.my_queue.pop(0)      # 如果该结点存在右子树，将此结点丢弃。


    def pre_order_digui(self, root, rootlist = None):
        """利用递归实现树的前序遍历"""
        if rootlist is None:
            rootlist = []

        if root:
            rootlist.append(root.elem)
            self.pre_order_digui(root.lchild, rootlist)
            self.pre_order_digui(root.rchild, rootlist)

        return rootlist

    def in_order_digui(self, root):
        """利用递归实现树的中序遍历"""
        if root == None: return

        self.in_order_digui(root.lchild)
        print(root.elem)
        self.in_order_digui(root.rchild)


    def post_order_digui(self, root):
        """利用递归实现树的后序遍历"""
        if root == None: return

        self.post_order_digui(root.lchild)
        self.post_order_digui(root.rchild)
        print(root.elem)


    def level_order_queue(self, root):
        """队列实现层遍历"""
        if root == None:return

        nodelist = []
        rootlist = []
        node = root
        rootlist.append(node)

        while rootlist:
            node = rootlist.pop(0)
            # print(node.elem)
            nodelist.append(node.elem)
            if node.lchild != None:
                rootlist.append(node.lchild)
            if node.rchild != None:
                rootlist.append(node.rchild)
        return nodelist


if __name__ == '__main__':
    """主函数"""
    elems = range(20)
    elemss = ['Taylor Swift', 'Country', 'Pop', 'Fearless', 'Red', '1989', 'Reputation',
              'Love Story', 'White Horse','We Are Never Ever Getting Back Together', 'I Knew You Were Trouble',
              'Shake It Off', 'Bad Blood', 'Look What You Made Me Do', 'Gorgeous']
    elemsss =  [33, 17, 50, 13, 20, 37, 58, 11, 15, 18, 25, 34, 41, 51, 66, 9]
    tree = Tree()
    for elem in elemsss:
        tree.add_elem(elem)

    # print ('递归实现前序遍历:')
    # print( tree.pre_order_digui(tree.root) )

    print ('递归实现中序遍历:')
    tree.in_order_digui(tree.root)

    # print ('递归实现后序遍历:')
    # tree.post_order_digui(tree.root)

    print('队列实现层遍历:')
    print(tree.level_order_queue(tree.root))