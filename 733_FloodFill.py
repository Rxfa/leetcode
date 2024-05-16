class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return

        def backtrack(image, r, c, color, oldColor):
            if r < 0 or r > len(image) - 1:
                return
    
            if c < 0 or c > len(image[r]) - 1:
                return

            if image[r][c] != oldColor or image[r][c] == color:
                return

            image[r][c] = color
            backtrack(image, r+1, c, color, oldColor)
            backtrack(image, r-1, c, color, oldColor)
            backtrack(image, r, c+1, color, oldColor)
            backtrack(image, r, c-1, color, oldColor)

        backtrack(image, sr, sc, color, image[sr][sc])
        return image