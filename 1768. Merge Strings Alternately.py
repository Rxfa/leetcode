class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer = 0
        merged = ""
        while pointer < len(word1) and pointer < len(word2):
            merged += word1[pointer]
            merged += word2[pointer]
            pointer += 1
        merged += word1[pointer:]
        merged += word2[pointer:]
        return merged
    