class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        if len(piles) == 3:
            return piles[1]
        
        i = len(piles)-2
        sum = 0
        
        while(i >= len(piles)/3):
            sum += piles[i]
            i -= 2
        
        return sum