from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_tree(ar, i,  l):
    root = None
    if i < l and ar[i] is not None:
        root = TreeNode(ar[i])
        root.left = insert_tree(ar, 2*i+1, l)
        root.right = insert_tree(ar, 2*i+2, l)
    return root


def in_order(root):
    if root:
        print(root.val, "::", root.left.val if root.left is not None else "N",
              root.right.val if root.right is not None else "")
        in_order(root.left)
        in_order(root.right)


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def check(root, sum):
            if root is not None:
                sum += root.val
                if sum == targetSum and root.left is None and root.right is None:
                    return True
                left = check(root.left, sum)
                right = check(root.right, sum)
                if left == True or right ==True:
                    return True
            return False
        return check(root, 0)


ar = [1]

tree_root = insert_tree(ar, 0, len(ar))
in_order(tree_root)

i = Solution()
call = i.hasPathSum(tree_root, 1)
print(" :: ", call)
