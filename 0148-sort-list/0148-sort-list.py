import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        pri_queue = []

        while head:
            heapq.heappush(pri_queue , head.val)
            head = head.next  

        print(pri_queue)

        dummy_node = ListNode()

        head1 = dummy_node

        while pri_queue:
            head1.next = ListNode()

            head1 = head1.next

            head1.val = heapq.heappop( pri_queue )


        return dummy_node.next

    