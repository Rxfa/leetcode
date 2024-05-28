class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        distances = [(abs(num - x), num) for num in arr]
        heapq.heapify(distances)
        res = [heapq.heappop(distances)[1] for _ in range(k)]
        res.sort()
        return res
