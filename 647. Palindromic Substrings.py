class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(left, right):
            count = 0
            while 0 <= left <= right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
            
        total_count = 0
        for i in range(len(s)):
            total_count += expand(i, i)
            total_count += expand(i, i + 1)
        
        return total_count    