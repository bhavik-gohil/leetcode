from typing import List, Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insert(self, nums):
        root = None
        length = len(nums)
        p = math.ceil(length/2)
        if length > 0:
            root = TreeNode(nums[p-1])
            root.left = self.insert(nums[0:p-1])
            root.right = self.insert(nums[p:length])
        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.insert(nums)


nums = [-1, 0, 1, 2]
# nums = [-10, -3, 0, 5, 9]
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]

ins = Solution()
call = ins.sortedArrayToBST(nums)
print("call :: ", call.val)
