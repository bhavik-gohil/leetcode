from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ""
        s2 = ""
        while l1 is not None or l2 is not None:
            if l1:
                s1 = str(l1.val) + s1
                l1 = l1.next
            if l2:
                s2 = str(l2.val)+s2
                l2 = l2.next

        s3 = str(int(s1)+int(s2))

        node = ListNode()
        cur = node
        l = len(s3)
        while l > 0:
            cur.val = int(s3[l-1])
            l = l - 1
            if l > 0:
                cur.next = ListNode()
                cur = cur.next

        return node


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        cur = node
        carry = 0

        while l1 is not None or l2 is not None:
            sum = carry
            carry = 0
            if l1:
                sum = sum + l1.val
                l1 = l1.next
            if l2:
                sum = sum + l2.val
                l2 = l2.next

            if sum > 9:
                sum = sum-10
                carry = 1

            cur.val = sum
            if l1 is not None or l2 is not None:
                cur.next = ListNode()
                cur = cur.next

        if carry == 1:
            cur.next = ListNode()
            cur = cur.next
            cur.val = carry

        return node
