class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        arr = []
        if not intervals:
            return [newInterval]
        for idx, interval in enumerate(intervals):
            if (
                newInterval[1] >= interval[0] >= newInterval[0] or
                newInterval[1] >= interval[1] >= newInterval[0]
            ):
                newInterval = [
                    min(interval[0], newInterval[0]), max(interval[1], newInterval[1])
                ]
            else:
                if interval[0] > newInterval[1]:
                    arr.append(newInterval)
                    return arr + intervals[idx:]
                arr.append(interval)
                if interval[0] <= newInterval[0] <= newInterval[1] <= interval[1]:
                    return arr + intervals[idx+1:]
        arr.append(newInterval)
        return arr
