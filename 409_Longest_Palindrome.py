class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        counter = dict()
        for char in s:
            counter[char] = 1 + counter.get(char, 0)

        even = 0
        odd = 0
        for num in counter.values():
            if num % 2 == 0:
                even += num
            else:
                even += num - 1
                odd = 1
        return even + odd