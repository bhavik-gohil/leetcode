from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        h = {}
        while head is not None:
            if h.get(head):
                return True
            h[head] = head.val
            head = head.next
        return False


ar = [3, 2, 0, -4]

i = Solution()
i.hasCycle()
print(":: ", i)
