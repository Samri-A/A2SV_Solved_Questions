# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current_head = head

        stack = deque()

        while current_head:
            while stack and current_head.val > stack[-1]:
                stack.pop()
            stack.append(current_head.val)
            
            current_head = current_head.next


       
        dummy = ListNode()
        head_ = dummy

        while stack:
            head_.next = ListNode()
            head_ = head_.next
            head_.val = stack.popleft()
            

        return dummy.next
