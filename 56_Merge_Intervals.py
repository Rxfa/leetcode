class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for idx, interval in enumerate(intervals):
            if idx == 0:
                res.append(interval)
            if res[-1][1] >= interval[0]:
                res[-1] = [min(res[-1][0], interval[0]), max(res[-1][1], interval[1])]
            else:
                res.append(interval)
        return res
