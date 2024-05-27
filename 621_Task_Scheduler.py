class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        task_counts = Counter(tasks)
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)
        time = 0
        cooldown = deque()
        while max_heap or cooldown:
            time += 1
            if max_heap:
                count = heappop(max_heap)
                count += 1
                if count != 0:
                    cooldown.append((count, time + n))
            if cooldown and cooldown[0][1] == time:
                heappush(max_heap, cooldown.popleft()[0])
        return time
