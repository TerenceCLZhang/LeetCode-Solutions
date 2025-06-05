# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head.next.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        slow = slow.next
        while (slow):
            temp = slow.next
            slow.next = prev
            prev, slow = slow, temp
        
        max_sum = 0
        left = head
        right = prev
        while (right):
            max_sum = max(max_sum, left.val + right.val)
            left = left.next
            right = right.next
        
        return max_sum

# Time: O(n)
# Space: O(1)