# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_end = dummy

        while True:
            kth_node = prev_end
            for _ in range(k):
                kth_node = kth_node.next
                if not kth_node:
                    return dummy.next

            group_next = kth_node.next

            prev = kth_node.next
            curr = prev_end.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev, curr = curr, temp

            temp = prev_end.next
            prev_end.next = kth_node
            prev_end = temp
