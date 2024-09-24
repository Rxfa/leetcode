class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        curr = ""
        for i in s:
            if i == " ":
                res += curr[::-1]
                res += i
                curr = ""
            else:
                curr += i
        return res + curr[::-1]
