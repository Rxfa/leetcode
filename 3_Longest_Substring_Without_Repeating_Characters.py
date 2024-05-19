class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        l = 0
        max_s = 0
        for idx, i in enumerate(s):
            max_s = max(max_s, len(chars))
            while i in chars:
                if s[l] in chars:
                    del chars[s[l]]
                l += 1
            chars[i] = idx
        return max(max_s, len(chars))