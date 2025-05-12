# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Using two passes

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        mid = length // 2

        curr = head
        for _ in range(mid):
            curr = curr.next
        
        return curr

# Time: O(n)
# Space: O(1)


# Using Floyd's Cycle Finding Algorithm / Hare-Tortoise Algorithm:

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

# Time: O(n)
# Space: O(1)
