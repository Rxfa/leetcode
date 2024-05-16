class Solution:
    def isValid(self, s: str) -> bool:
        closing_to_opening = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        waiting_list = []
        if len(s) % 2 != 0:
            return False
        for i in range(len(s) - 1, -1, -1):
            if s[i] in closing_to_opening:
                waiting_list.append(closing_to_opening[s[i]])
                continue
            if not waiting_list or s[i] != waiting_list.pop():
                return False
        return not waiting_list
