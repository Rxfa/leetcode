class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        memo = {}
        
        def backtrack(start):
            if start == len(s):
                return True
            if start in memo:
                return memo[start]
            
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set and backtrack(end):
                    memo[start] = True
                    return True
            
            memo[start] = False
            return False
        
        return backtrack(0)
