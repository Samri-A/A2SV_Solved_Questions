# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummyhead = head
        slow = dummyhead
        fast = head
        
        while n > 0:
            n -= 1
            fast = fast.next
        
        if not fast:
            return dummyhead.next
        
        

        while fast.next:
            fast = fast.next 
            slow = slow.next



        slow.next = slow.next.next
        return dummyhead