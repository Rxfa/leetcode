import math

class Solution:
    def hammingWeight(self, n: int) -> int:
        num = n
        set_bits = 0
        while num > 0:
            lowest_power = math.floor(math.log(num, 2))
            num -= math.pow(2, lowest_power)
            set_bits += 1
        return set_bits
        