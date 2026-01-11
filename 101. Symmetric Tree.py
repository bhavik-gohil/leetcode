from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def new_tree(ar, i,  l):
    root = None
    if i < l and ar[i] is not None:
        root = TreeNode(ar[i])
        root.left = new_tree(ar, 2*i+1, l)
        root.right = new_tree(ar, 2*i+2, l)
    return root


def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.val, " - ",
              root.left.val if root.left is not None else "*", root.right.val if root.right is not None else "*")
        in_order_traversal(root.right)


class Solution:
    def rec(self, left, right):
        if (left is not None and right is None) or (left is None and right is not None):
            return False
        if left is not None and right is not None:
            if left.val != right.val:
                return False
            result = self.rec(left.left, right.right)
            if result is False:
                return False
            result = self.rec(left.right, right.left)
            if result is False:
                return False
        return True
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.rec(root.left, root.right)


ar = [1,2,2,3,4,4,3]
tree_root = new_tree(ar, 0, len(ar))
print("---tree_root", tree_root.val)
in_order_traversal(tree_root)

ins = Solution()
call = ins.isSymmetric(tree_root)
print("\ncall :: ", call)
