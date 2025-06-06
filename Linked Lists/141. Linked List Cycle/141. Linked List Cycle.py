# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Floyd's Cycle Finding Algorithm / Hare-Tortoise Algorithm:
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast is slow:
                return True
                
        return False

# Time: O(n)
# Space: O(1)