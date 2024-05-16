# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = None
        currentNode = ListNode()
        if not list1 and not list2:
            return
        while list1 or list2:
            if not list1:
                currentNode.next = list2
                list2 = None
            elif not list2:
                currentNode.next = list1
                list1 = None
            else:
                if list1.val <= list2.val:
                    currentNode.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    currentNode.next = ListNode(list2.val)
                    list2 = list2.next
            currentNode = currentNode.next

            if not merged and currentNode:
                merged = currentNode
        return merged if merged else currentNode