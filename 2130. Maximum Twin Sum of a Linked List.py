# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        curr = slow
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp

        max_twin_sum = 0

        start = head
        end = prev
        while start and end:
            summ = start.val + end.val
            max_twin_sum = max(max_twin_sum, summ)
            start = start.next
            end = end.next

        return max_twin_sum
