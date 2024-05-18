# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        current = head
        values = []
        while current:
            values.append(current)
            current = current.next

        for idx, node in enumerate(values):
            if idx == 0:
                node.next = None
            else:
                node.next = values[idx-1]

        return values[-1]