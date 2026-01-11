from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_node = ListNode()
        current_node = new_node

        flag = True
        while flag:
            if list1 and list2:
                if list1.val <= list2.val:
                    current_node.next = list1
                    list1 = list1.next
                else:
                    current_node.next = list2
                    list2 = list2.next

                current_node = current_node.next
            else:
                flag = False

        current_node.next = list1 if list1 else list2

        return new_node.next


def insert_node(list1):
    first_list_node = ListNode() if list1 else None
    current_list_node = first_list_node
    for i in list1:
        current_list_node.val = i
        current_list_node.next = ListNode()
        current_list_node = current_list_node.next
    return first_list_node


list1 = [1, 2, 4]
list2 = [1, 3, 4]
inserted_node_1 = insert_node(list1)
inserted_node_2 = insert_node(list2)


def read_node(node):
    while node and node.next:
        print("->", node.val)
        node = node.next


print("--inserted_node_1")
read = read_node(inserted_node_1)
print("--inserted_node_2")
read = read_node(inserted_node_2)


ins = Solution()
call = ins.mergeTwoLists(inserted_node_1, inserted_node_2)
print("--call--", call)

read = read_node(call)
