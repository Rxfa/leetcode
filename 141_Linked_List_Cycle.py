# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cycled_through = set()
        current = head
        while current not in cycled_through:
            if not current:
                return False
            cycled_through.add(current)
            current = current.next
        return True
        