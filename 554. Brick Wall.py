class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_count = defaultdict(int)
        
        for row in wall:
            width = 0
            for i in range(len(row) - 1):
                width += row[i]
                edge_count[width] += 1
        
        if not edge_count:
            return len(wall)
        return len(wall) - max(edge_count.values())