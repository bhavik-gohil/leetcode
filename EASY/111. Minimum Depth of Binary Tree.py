from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_tree(ar, i, l):
    root = None
    if i < l and ar[i] is not None:
        root = TreeNode(ar[i])
        root.left = insert_tree(ar, 2*i+1, l)
        root.right = insert_tree(ar, 2*i+2, l)
    return root


def in_order(root):
    if root:
        print(root.val, "::", root.left.val if root.left is not None else "-",
              root.right.val if root.right is not None else "")
        in_order(root.left)
        in_order(root.right)


class Solution:
    def check(self, root, depth):
        if root is None:
            return root, root

        # depth = depth + 1
        left_depth = depth
        right_depth = depth
        print("..", depth, left_depth, right_depth)

        if root.left is not None:
            d = self.check(root.left, depth)
            left_depth = left_depth + 1 + d

        if root.right is not None:
            d = self.check(root.right, depth)
            right_depth = right_depth + 1 + d

        # if left_depth == 0 and right_depth == 0:
        #     left_depth = left_depth + 1
        #     right_depth = right_depth + 1
        #     print("--", depth, left_depth, right_depth)

        print("-", depth, left_depth, right_depth)
        return left_depth if left_depth > right_depth else right_depth

    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.check(root, 0)


ar = [-9, -3, 2, None, 4, 4, 0, -6, None, -5]
# ar = [3, 9, 20, None, None, 15, 7]
# ar = [2, None, 3, None, 4, None, 5, None, 6]

tree_root = insert_tree(ar, 0, len(ar))

print("-------------", tree_root.val)
in_order(tree_root)
print("-------------")

i = Solution()
call = i.minDepth(tree_root)
print(" :: ", call)
