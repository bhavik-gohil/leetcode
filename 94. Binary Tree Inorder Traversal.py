from typing import List, Optional


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_tree(arr, i, length):
    head = TreeNode()
    head.val = None
    if i < length:
        head = TreeNode(arr[i])
        head.left = insert_tree(arr, i+1, length)
        head.right = insert_tree(arr, i+2, length)
    return head


# def in_order(head):
#     if head and head.val:
#         in_order(head.left)
#         print(head.val)
#         in_order(head.right)


# def pre_order(head):
#     if head and head.val:
#         print(head.val)
#         pre_order(head.left)
#         pre_order(head.right)


# def post_order(head):
#     if head and head.val:
#         post_order(head.left)
#         post_order(head.right)
#         print(head.val)


# [
#     1,
#     2,                  3,
#     4,          5,      null,8,
#     null,null,  6, 7,         9]

class Solution:
    def in_order(self, head, arr):
        if head is not None and head.val is not None:
            self.in_order(head.left, arr)
            arr.append(head.val)
            self.in_order(head.right, arr)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.in_order(root, arr)
        return arr


arr = [1, None, 0, 3]
tree_head = insert_tree(arr, 0, len(arr))
print("tree_head :: ", tree_head.val, tree_head.left.val,
      tree_head.right.val, tree_head.right.left.val, tree_head.right.right)
# print("-------in_order------")
# in_order(tree_head)
# print("-------pre_order------")
# pre_order(tree_head)
# print("-------post_order------")
# post_order(tree_head)

ins = Solution()
call = ins.inorderTraversal(tree_head)
print("call :: ", call)
