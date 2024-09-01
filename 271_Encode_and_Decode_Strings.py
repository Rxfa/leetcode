class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        j = 0
        while i < len(s):
            while s[i] != "#":
                i += 1
            length = int(s[j:i])
            j = i + length + 1
            word = s[i+1:j]
            res.append(word)
            i = j
        return res
    