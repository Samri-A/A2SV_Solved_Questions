# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_ = head
       

        current_head = head
        last = current_head.val
        while current_head.next:

            while last > current_head.next.val:
                current_head.next = current_head.next.next
                current_head = current_head.next
            
