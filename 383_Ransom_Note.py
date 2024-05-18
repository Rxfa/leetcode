class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) == len(magazine) == 1:
            return ransomNote == magazine

        letters = dict()
        for char in magazine:
            letters[char] = 1 + letters.get(char, 0)

        for char in ransomNote:
            if char in letters and letters.get(char, 0) > 0:
                letters[char] -= 1
            else:
                return False
        return True