# Time complexity is O(1)
# Space complexity is O(1)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row_idx, row in enumerate(board):
            for col_idx, cell in enumerate(row):
                if cell.isdigit():
                    if cell in rows[row_idx]:
                        return False
                    if cell in cols[col_idx]:
                        return False
                    box_idx = (row_idx // 3) * 3 + (col_idx // 3)
                    if cell in boxes[box_idx]:
                        return False

                    rows[row_idx].add(cell)
                    cols[col_idx].add(cell)
                    boxes[box_idx].add(cell)
        return True
