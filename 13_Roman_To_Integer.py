class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        num =  0
        for idx, symbol in enumerate(s):
            value_to_add = symbols[symbol]
            if idx < len(s) - 1 and symbols[symbol] < symbols[s[idx+1]]:
                value_to_add *= -1
            num += value_to_add
        return num