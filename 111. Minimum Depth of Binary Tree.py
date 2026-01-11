from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def insert_tree(ar, i, l):
#     root = None
#     if i < l and ar[i] is not None:
#         root = TreeNode(ar[i])
#         root.left = insert_tree(ar, 2*i+1, l)
#         n = 2
#         if root.left is None:
#             n = 1
#         root.right = insert_tree(ar, n*i+2, l)
#     return root

def insert_tree(ar, i,  l):
    root = None
    if i < l and ar[i] is not None:
        root = TreeNode(ar[i])
        root.left = insert_tree(ar, 2*i+1, l)
        root.right = insert_tree(ar, 2*i+2, l)
    return root


def in_order(root):
    if root:
        in_order(root.left)
        print(root.val, "::", root.left.val if root.left is not None else "N",
              root.right.val if root.right is not None else "")
        in_order(root.right)


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root, dep):
            if root is None:
                return dep, dep

            dep += 1

            left_l, left_r = depth(root.left, dep)
            right_l, right_r = depth(root.right, dep)

            l = left_l if left_l < left_r else left_r
            r = right_l if right_l < right_r else right_r

            if left_l == left_r and left_l == dep:
                l = r

            if right_l == right_r and right_r == dep:
                r = l

            return l, r

        l, r = depth(root, 0)

        return l if l < r else r


ar = [-9, -3, 2, None, 4, 4, 0, -6, None, -5]
# ar = [3, 9, 20, None, None, 15, 7]
# ar = [2, None, 3, None, 4, None, 5, None, 6]


tree_root = insert_tree(ar, 0, len(ar))
in_order(tree_root)

i = Solution()
call = i.minDepth(tree_root)
print(" :: ", call)
