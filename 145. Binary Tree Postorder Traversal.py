from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []

        def post_order(r):
            if r is not None:
                post_order(r.left)
                post_order(r.right)
                traversal.append(r.val)

        post_order(root)
        return traversal
