class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        def clearRowAndCol(row, col):
            for i in range(n):
                matrix[i][col] = 0
            for i in range(m):
                matrix[row][i] = 0
        flagged = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    flagged.add((i, j))

        for row, col in flagged:
            clearRowAndCol(row, col)
            