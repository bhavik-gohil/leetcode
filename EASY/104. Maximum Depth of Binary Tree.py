from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree(ar, i, l):
    root = None
    if i < l and ar[i] is not None:
        root = TreeNode(ar[i])
        root.left = create_tree(ar, 2*i+1, l)
        root.right = create_tree(ar, 2*i+2, l)
    return root


def in_order(root):
    if root:
        in_order(root.left)
        print(root.val, "::", root.left.val if root.left is not None else "",
              root.right.val if root.right is not None else "")
        in_order(root.right)


class Solution:
    def depth(self, root, count):
        if root:
            left_count = self.depth(root.left, count + 1)
            right_count = self.depth(root.right, count + 1)
            count = left_count if left_count > right_count else right_count
        return count

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root, 0)


ar = [3, 9, 20, None, None, 15, 7]
tree_root = create_tree(ar, 0, len(ar))
in_order(tree_root)

ins = Solution()
call = ins.maxDepth(tree_root)
print("\ncall :: ", call)
