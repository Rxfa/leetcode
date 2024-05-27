class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        used = set()
        def rec(row, col, idx):
            if idx == len(word):
                return True
            if (
                row < 0 or row >= len(board) or 
                col < 0 or col >= len(board[0]) or
                board[row][col] != word[idx] or (row, col) in used
            ):
                return False
            used.add((row, col))
            if (
                rec(row + 1, col, idx + 1) or
                rec(row - 1, col, idx + 1) or
                rec(row, col + 1, idx + 1) or
                rec(row, col - 1, idx + 1)
            ):
                return True
            used.remove((row, col))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if rec(i, j, 0):
                    return True
        return False
