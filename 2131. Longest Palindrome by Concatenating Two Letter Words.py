class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = defaultdict(int)
        palindrome_length = 0
        has_center = 0
        
        for word in words:
            count[word] += 1
        
        for word, freq in count.items():
            if word[0] == word[1]: 
                palindrome_length += (freq // 2) * 2 
                if freq % 2 == 1:  
                    has_center = 1
            else:
                reverse_word = word[::-1]
                if reverse_word in count:
                    palindrome_length += min(freq, count[reverse_word]) * 2 
        return palindrome_length + has_center * 2 
