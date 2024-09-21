class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        idx = 1
        prev_word = strs[0]
        longest_common_prefix = ""
        while idx <= len(prev_word):
            for word in strs:
                if prev_word[:idx] != word[:idx]:
                    return longest_common_prefix
            longest_common_prefix = prev_word[:idx]
            idx += 1
        return longest_common_prefix
