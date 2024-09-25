class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        mat_size = r * c
        new_size = len(mat) * len(mat[0])
        if new_size != mat_size:
            return mat

        nums = deque([])
        row = col = 0
        for row in mat:
            for num in row:
                nums.append(num)
        

        res = [[0 for _ in range(c)] for i in range(r)]
        for i in range(r):
            for j in range(c):
                res[i][j] = nums.popleft()
        return res