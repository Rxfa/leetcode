class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = [(-freq, word) for word, freq in Counter(words).items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
