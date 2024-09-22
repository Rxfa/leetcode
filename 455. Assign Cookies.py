class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        children_idx = 0
        cookie_idx = 0
        matchings = 0
        while children_idx < len(g) and cookie_idx < len(s):
            if g[children_idx] <= s[cookie_idx]:
                matchings += 1
                children_idx += 1
            cookie_idx += 1
        return matchings
