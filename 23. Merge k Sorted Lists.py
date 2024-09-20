# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        heap = []
        for idx, i in enumerate(lists):
            if i:
                # The has to have three fields in case there is a tie with the comparison of val (ListNode has no cmp function)
                heapq.heappush(heap, (i.val, idx, i))
        
        dummy = ListNode()
        curr = dummy
        
        while heap:
            val, idx, node = heapq.heappop(heap)
            
            curr.next = node
            curr = curr.next
            
            if node.next:  
                heapq.heappush(heap, (node.next.val, idx, node.next))
        head = dummy.next
        return head