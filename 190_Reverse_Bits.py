class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 0
        while n:
            if n % 2 == 1:
                res += int(math.pow(2, 31-i))
            i += 1
            n >>= 1
        return res
