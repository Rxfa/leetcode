class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def paths(r, c):
            if (c == 1) or (r == 1):
                return 1
            if (r, c) in cache:
                return cache[(r, c)]
            right = paths(r - 1, c) if r > 1 else 0
            down = paths(r, c - 1) if c > 1 else 0
            cache[(r, c)] = right + down
            return right + down
        return paths(m, n)
