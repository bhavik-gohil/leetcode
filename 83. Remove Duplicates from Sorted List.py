
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insert_node(list1):
    first_list_node = ListNode() if list1 else None
    current_list_node = first_list_node
    for i in list1:
        current_list_node.val = i
        current_list_node.next = ListNode()
        current_list_node = current_list_node.next
    return first_list_node


def read_node(node):
    while node and node.next:
        print("->", node.val)
        node = node.next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        og_head = head
        next_node = head.next
        while next_node:
            if head.val == next_node.val:
                next_node = next_node.next
                head.next = next_node
            else:
                head = head.next
                next_node = next_node.next
        return og_head


arr = [1,1,2,3,3]

inserted_node = insert_node(arr)
read_node(inserted_node)
print("---read_node ^", inserted_node)

ins = Solution()
call = ins.deleteDuplicates(inserted_node)
print("call: ", call)

read_node(call)
print("---call ^")
