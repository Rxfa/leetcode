class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def max_local(r, c):
            max_num = -1
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    max_num = max(max_num, grid[i][j])
            return max_num
        res = []
        for i in range(1, len(grid) - 1):
            row = []
            for j in range(1, len(grid[0]) - 1):
                row.append(max_local(i, j))
            res.append(row)
        return res
