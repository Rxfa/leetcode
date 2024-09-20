class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        tmp = abs(x)
        
        while tmp:
            digit = tmp % 10
            tmp = tmp // 10
            
            if res > (2**31 - 1) // 10:
                return 0
            
            res = res * 10 + digit
        
        res = res if x > 0 else -res
        
        if -2**31 <= res <= 2**31 - 1:
            return res
        return 0

