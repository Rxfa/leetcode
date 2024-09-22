class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrom(word):
            l, r = 0, len(word) - 1
            while l < r and word[l] == word[r]:
                l += 1
                r -= 1
            return l >= r

        for i in words:
            if isPalindrom(i):
                return i
        return ""
        