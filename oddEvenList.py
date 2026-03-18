# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        odd_dummy = ListNode()
        odd = odd_dummy
        even_dummy = ListNode()
        even = even_dummy

        while head:
            odd.next = ListNode(head.val)
            odd = odd.next
            head = head.next
            if head: 
                even.next = ListNode(head.val)
                even = even.next
                head = head.next
                  

        odd.next = even_dummy.next
        return odd_dummy.next 
