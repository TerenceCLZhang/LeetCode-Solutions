# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        decimal = 0
        curr = head
        while curr:
            decimal = (decimal << 1) | curr.val
            curr = curr.next
        return decimal

# Time: O(n)
# Space: O(1)