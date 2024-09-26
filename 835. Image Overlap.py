class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        def count_overlap(row_shift, col_shift):
            overlap = 0
            for r in range(n):
                for c in range(n):
                    if 0 <= r + row_shift < n and 0 <= c + col_shift < n:
                        overlap += img1[r][c] * img2[r + row_shift][c + col_shift]
            return overlap
        
        max_overlap = 0
        
        for row_shift in range(-n + 1, n):
            for col_shift in range(-n + 1, n):
                max_overlap = max(max_overlap, count_overlap(row_shift, col_shift))
        
        return max_overlap
