# 节点类
class Node:
    # 用类成员函数进行节点初始化
    def __init__(self, value):
        self.value = value
        self.lchild = None
        self.rchild = None


# BST树类
class BST:
    # 用类成员函数进行BST初始化
    def __init__(self, node_list):
        self.root = Node(node_list[0])
        for value in node_list[1:]:
            self.insert(value)

    # 搜索拥有某值的节点操作
    def search(self, node, parent, value):
        if node is None:
            return False, node, parent
        if node.value == value:
            return True, node, parent
        # 小的在左孩子，大于等于的在右孩子
        if node.value > value:
            return self.search(node.lchild, node, value)
        else:
            return self.search(node.rchild, node, value)

    # 插入某值的节点操作
    def insert(self, value):
        flag, n, p = self.search(self.root, self.root, value)
        if not flag:
            new_node = Node(value)
            if value > p.value:
                p.rchild = new_node
            else:
                p.lchild = new_node

    # 删除某值的节点
    def delete(self, value):
        flag, n, p = self.search(self.root, self.root, value)
        if flag is False:
            print("Can't find the key! Delete failed!")
        else:
            # 当左子树为空时
            if n.lchild is None:
                if n == p.lchild:
                    p.lchild = n.rchild
                else:
                    p.rchild = n.rchild

            # 当右子树为空时
            elif n.rchild is None:
                if n == p.lchild:
                    p.lchild = n.lchild
                else:
                    p.rchild = n.lchild
            else:
                # 当左右都不为空时，选择右子树
                pre = n.rchild
                if pre.lchild is None:
                    # 如果左子树为空，直接将右子树上移
                    n.value = pre.value
                    n.rchild = pre.rchild
                else:
                    # 如果左子树不为空，直接迭代到左子树根节点
                    next = pre.lchild
                    while next.lchild is not None:
                        # 迭代，在这里写代码，写代码时候删除pass
                        pre = next
                        next = next.lchild
                    n.value = next.value
                    pre.lchild = next.rchild

    # 先序遍历
    def pre_order_traverse(self, node):
        if node is not None:
            print(node.value)
            self.pre_order_traverse(node.lchild)
            self.pre_order_traverse(node.rchild)

    # 中序遍历
    def in_order_traverse(self, node):
        if node is not None:
            self.in_order_traverse(node.lchild)
            print(node.value)
            self.in_order_traverse(node.rchild)

    # 后序遍历
    def post_order_traverse(self, node):
        if node is not None:
            self.post_order_traverse(node.lchild)
            self.post_order_traverse(node.rchild)
            print(node.value)


array = [7, 5, 3, 4, 1, 2, 8]
bst = BST(array)
"""
                    7
                  .  .
                5     8
              .
            3
          .  .
        1     4
         .
          2
"""
bst.pre_order_traverse(bst.root)
print("*"*10)
bst.in_order_traverse(bst.root)
print("*"*10)



array2 = [5,3,2,4,3.1,3.05,3.5,3.06]
bst2 = BST(array2)
bst2.pre_order_traverse(bst2.root)
"""
                    5
                  .
                3
              .    .
            2       4
                   .
                  3.1
                .    .
              3.05   3.5
                .
                3.06


"""
print("*"*10)
bst2.delete(3)
bst2.pre_order_traverse(bst2.root)
"""
                    5
                  .
                3.05
               .    .
             2       4
                      .
                      3.1
                     .     .
                   3.06    3.5
              

"""
