# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp

        left = head
        right = prev
        while right.next:
            temp1 = left.next
            temp2 = right.next

            left.next = right
            right.next = temp1

            left = temp1
            right = temp2

# Time: O(n)
# Space: O(1)