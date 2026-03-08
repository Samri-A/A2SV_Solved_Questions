# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = None

        while head:
            node = ListNode(head.val) 
            node.next = dummy_node
            dummy_node = node
            head = head.next


        return dummy_node

