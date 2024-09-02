class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        heap = []
        for i in stones:
            heapq.heappush(heap, -i)

        while len(heap) > 1:
            y = abs(heapq.heappop(heap))
            x = abs(heapq.heappop(heap))
            if x != y:
                y = - (y - x)
                heapq.heappush(heap, y)
        if len(heap):
            return -heap[0]
        return 0