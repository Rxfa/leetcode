class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) < 3:
            return n == 1 and sum(flowerbed) == 0
            
        valid_plots = 0
        for idx, plot in enumerate(flowerbed):
            if plot == 1:
                continue
                
            if idx == 0 and flowerbed[idx+1] == 0:
                valid_plots += 1
                flowerbed[idx] = 1
            elif (idx == len(flowerbed) - 1) and flowerbed[idx-1] == 0:
                valid_plots += 1
                flowerbed[idx] = 1
            elif flowerbed[idx-1] == 0 and flowerbed[idx+1] == 0:
                valid_plots += 1
                flowerbed[idx] = 1
        return valid_plots >= n
