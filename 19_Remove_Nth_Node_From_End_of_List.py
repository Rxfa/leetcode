# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def remove(node):
            next_node = node.next
            node.next = next_node.next
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next

        if size == 1:
            return
        if size-n <= 0:
            return head.next
        
        curr = head
        for _ in range(1, size-n):
            curr = curr.next
        remove(curr)
        return head
    