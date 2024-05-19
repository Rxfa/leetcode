import math
from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = {}
        heap = []
        for point in points:
            x, y = point
            distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
            if distance in d:
                d[distance].append(point)
            else:
                d[distance] = [point]
            heappush(heap, distance)
        return [d[heappop(heap)].pop() for _ in range(k)]
