class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_w = {word.lower() for word in banned}
        count = {}
        mostCommon = ("", 0)
        words = re.split('\W+', paragraph)
        for word in words:
            i = word.lower()
            if i not in banned:
                count[i] = count.get(i, 0) + 1
                if count[i] > mostCommon[1]:
                    mostCommon = (i, count[i])
        return mostCommon[0]
