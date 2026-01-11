from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def check(self, root, depth):
        left_depth = depth
        right_depth = depth
        is_balanced = True

        if root is not None:
            if root.left is not None and root.right is None:
                ld, rd, is_bal = self.check(root.left, depth)
                left_depth = depth + 1 + (ld if ld > rd else rd)

                return left_depth, right_depth, left_depth <= 1
            elif root.left is None and root.right is not None:
                ld, rd, is_bal = self.check(root.right, depth)
                right_depth = depth + 1 + (ld if ld > rd else rd)

                return left_depth, right_depth, right_depth <= 1
            else:
                if root.left is not None:
                    ld, rd, is_bal = self.check(root.left, depth)
                    left_depth = depth + 1 + (ld if ld > rd else rd)

                    if is_bal == False or (abs(ld-rd) > 1 and left_depth > 1):
                        return left_depth, right_depth, False

                if root.right is not None:
                    ld, rd, is_bal = self.check(root.right, depth)
                    right_depth = depth + 1 + (ld if ld > rd else rd)

                    if is_bal == False or (abs(ld-rd) > 1 and right_depth > 1):
                        return left_depth, right_depth, False

        return left_depth, right_depth, is_balanced

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        left_depth, right_depth, is_balanced = self.check(root, 0)
        return False if is_balanced == False or abs(left_depth-right_depth) > 1 else True


ar = [1, 2, 2, 3, 3, None, None, 4, 4]
i = Solution()
i.isBalanced(ar)
