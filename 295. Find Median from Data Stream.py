class MedianFinder:
    def __init__(self):
        self.max_heap = [] 
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)

        if (self.max_heap and self.min_heap and 
            (-self.max_heap[0] > self.min_heap[0])):
            value_to_move = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, value_to_move)

        if len(self.max_heap) > len(self.min_heap) + 1:
            value_to_move = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, value_to_move)
        elif len(self.min_heap) > len(self.max_heap):
            value_to_move = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -value_to_move)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
