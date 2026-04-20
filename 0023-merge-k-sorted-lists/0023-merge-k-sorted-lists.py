# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_node = ListNode()
        head = ListNode()

        dummy_node.next = head

        def merge(l1, l2):
            dummy_node = ListNode(0)
            current = dummy_node
            while l1 and l2:
                
                if l1.val < l2.val :
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                
                current = current.next
                
                
            if l1:
                current.next = l1
            elif l2:
                current.next = l2


                
            return dummy_node.next

        left = 1

        if len(lists) == 0:
            return None

        head = lists[0]

        while left < len(lists):
                new_l = merge(head , lists[left])

                head = new_l

                left += 1

        return head
            


