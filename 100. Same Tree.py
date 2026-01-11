from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree(arr, i, length):
    head = TreeNode(None)
    if i < length:
        head.val = arr[i]
        head.left = create_tree(arr, 2*i+1, length)
        head.right = create_tree(arr, 2*i+2, length)
    return head


def in_order(head):
    if head is not None and head.val is not None:
        in_order(head.left)
        print(head.val)
        in_order(head.right)


class Solution:
    def isSame(self, p, q):
        if (p is not None and q is None) or (p is None and q is not None):
            return False
        if p is not None and q is not None:
            if p.val != q.val:
                return False
            result = self.isSame(p.left, q.left)
            if result is False:
                return False
            result = self.isSame(p.right, q.right)
            if result is False:
                return False
        return True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.isSame(p, q)


p = [1, 2, 2, 3, 4, 4, 3]
q = [1, None, 2]
p_head = create_tree(p, 0, len(p))
q_head = create_tree(q, 0, len(q))
print("----------------p_head", p_head.val)
in_order(p_head)
print("----------------q_head", q_head.val)
in_order(q_head)

ins = Solution()
call = ins.isSameTree(p_head, q_head)
print("call :: ", call)
