class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        target = {
            "b": 1,
            "a": 1,
            "l": 2,
            "o": 2,
            "n": 1
        }
        occ = 0
        while True:
            for key, val in target.items():
                if count.get(key, -1) < val:
                    return occ
                count[key] -= val
            occ += 1 
