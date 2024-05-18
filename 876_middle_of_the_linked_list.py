# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        nodes = []
        while current:
            nodes.append(current)
            current = current.next
        return nodes[len(nodes) // 2]
