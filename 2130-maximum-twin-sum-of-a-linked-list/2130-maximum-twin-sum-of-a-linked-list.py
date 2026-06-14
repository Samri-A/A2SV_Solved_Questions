# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        fast = head
        slow =  head
        first_half = []
        second_half = []

        while fast:
            first_half.append(slow.val)
            slow = slow.next
            
            fast = fast.next.next

        while slow:
            second_half.append(slow.val)
            slow = slow.next
        
        second_half.reverse()

        ans = 0 

        i = 0
        while i < len(second_half):
            ans = max( ans,second_half[i] + first_half[i])
            i+=1
            
        return ans
        
