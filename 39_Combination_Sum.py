class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cur = []
        res = []
        def dfs(i, total):
            if total == target: 
                res.append(cur.copy())
                return
            if total > target: return
            if i >= len(candidates): return
            cur.append(candidates[i])
            dfs(i, total + candidates[i])
            cur.pop()
            dfs(i+1, total)
        dfs(0, 0)
        return res
